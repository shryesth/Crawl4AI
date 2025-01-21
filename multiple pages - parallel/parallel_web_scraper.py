import os
import re
import sys
import psutil
import asyncio
import requests
from urllib.parse import urlparse
from xml.etree import ElementTree

__location__ = os.path.dirname(os.path.abspath(__file__))
__output__ = os.path.join(__location__, "output")

# Append parent directory to system path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from typing import List
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

async def crawl_parallel(urls: List[str], max_concurrent: int = 3):
    print("\n=== Parallel Crawling with Browser Reuse + Memory Check ===")

    # We'll keep track of peak memory usage across all tasks
    peak_memory = 0
    process = psutil.Process(os.getpid())

    def log_memory(prefix: str = ""):
        nonlocal peak_memory
        current_mem = process.memory_info().rss  # in bytes
        if current_mem > peak_memory:
            peak_memory = current_mem
        print(f"{prefix} Current Memory: {current_mem // (1024 * 1024)} MB, Peak: {peak_memory // (1024 * 1024)} MB")

    # Minimal browser config
    browser_config = BrowserConfig(
        headless=True,
        verbose=False,   # corrected from 'verbos=False'
        extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
    )
    crawl_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)

    # Create the crawler instance
    crawler = AsyncWebCrawler(config=browser_config)
    await crawler.start()

    try:
        # We'll chunk the URLs in batches of 'max_concurrent'
        parent_folder_created = False
        parent_folder = None
        success_count = 0
        fail_count = 0
        for i in range(0, len(urls), max_concurrent):
            batch = urls[i : i + max_concurrent]
            tasks = []

            for j, url in enumerate(batch):
                # Unique session_id per concurrent sub-task
                session_id = f"parallel_session_{i + j}"
                task = crawler.arun(url=url, config=crawl_config, session_id=session_id)
                tasks.append(task)

            # Check memory usage prior to launching tasks
            log_memory(prefix=f"Before batch {i//max_concurrent + 1}: ")

            # Gather results
            results = await asyncio.gather(*tasks, return_exceptions=True)

            # Check memory usage after tasks complete
            log_memory(prefix=f"After batch {i//max_concurrent + 1}: ")

            # Evaluate results
            for url, result in zip(batch, results):
                if isinstance(result, Exception):
                    print(f"Error crawling {url}: {result}")
                    fail_count += 1
                elif result.success:
                    success_count += 1
                    print(f"Successfully crawled: {url}")
    
                    # Parse the URL to get the domain
                    parsed_url = urlparse(url)
                    domain = parsed_url.netloc.replace('.', '_')
                    
                    # Create the parent folder based on the domain if not already created
                    if not parent_folder_created:
                        parent_folder = domain
                        if not os.path.exists(parent_folder):
                            os.makedirs(parent_folder)
                        parent_folder_created = True
                    
                    # Create a safe filename for the markdown file
                    safe_filename = re.sub(r'[^\w\-_\. ]', '_', parsed_url.path.strip('/'))
                    if not safe_filename:
                        safe_filename = 'index'
                    filepath = os.path.join(parent_folder, f'{safe_filename}.md')
                    
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(result.markdown)
                    
                    print(f"Markdown length: {len(result.markdown_v2.raw_markdown)}")
                else:
                    fail_count += 1
                    print(f"Failed: {url} - Error: {result.error_message}")

        print(f"\nSummary:")
        print(f"  - Successfully crawled: {success_count}")
        print(f"  - Failed: {fail_count}")

    finally:
        print("\nClosing crawler...")
        await crawler.close()
        # Final memory log
        log_memory(prefix="Final: ")
        print(f"\nPeak memory usage (MB): {peak_memory // (1024 * 1024)}")

def get_urls(site_map_url: str) -> List[str]:
    """
    Fetches all URLs from the Pydantic AI documentation.
    Uses the sitemap (https://ai.pydantic.dev/sitemap.xml) to get these URLs.
    
    Returns:
        List[str]: List of URLs
    """            
    try:
        response = requests.get(site_map_url)
        response.raise_for_status()
        
        # Parse the XML
        root = ElementTree.fromstring(response.content)
        
        # Extract all URLs from the sitemap
        # The namespace is usually defined in the root element
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = [loc.text for loc in root.findall('.//ns:loc', namespace)]
        
        return urls
    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        return []

async def main():
    site_map_url = "https://docs.crawl4ai.com/sitemap.xml"
    urls = get_urls(site_map_url)
    if urls:
        print(f"Found {len(urls)} URLs to crawl")
        await crawl_parallel(urls)
    else:
        print("No URLs found to crawl")  

if __name__ == "__main__":
    asyncio.run(main())
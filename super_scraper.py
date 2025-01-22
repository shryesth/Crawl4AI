import os
import re
import sys
import asyncio
import logging
import requests
from dotenv import load_dotenv
from typing import List
from urllib.parse import urlparse
from xml.etree import ElementTree
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

# Load environment variables from a .env file
load_dotenv()

class WebScraper:
    def __init__(self, output_dir: str = "output", max_concurrent: int = 3):
        self.output_dir = output_dir
        self.max_concurrent = max_concurrent
        os.makedirs(self.output_dir, exist_ok=True)

        # Set up basic logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger('WebScraper')

    async def scrape_single(self, url: str):
        self.logger.info(f"Starting to scrape single URL: {url}")
        browser_config = BrowserConfig(headless=True)

        async with AsyncWebCrawler(config=browser_config) as crawler:
            try:
                result = await crawler.arun(url=url)
                if result.success:
                    self.logger.info(f"Successfully crawled single URL: {url}")
                    self._save_markdown(result.markdown, url)
                else:
                    self.logger.error(f"Failed to crawl URL: {url} - Error: {result.error_message}")
            except Exception as e:
                self.logger.error(f"Error during scraping single URL {url}: {e}")

    async def scrape_multiple(self, urls: List[str]):
        self.logger.info("Starting to scrape multiple URLs")
        await self._crawl_parallel(urls)

    async def scrape_from_sitemap(self, sitemap_url: str):
        urls = self._get_urls_from_sitemap(sitemap_url)
        if urls:
            self.logger.info(f"Found {len(urls)} URLs to crawl from sitemap.")
            await self._crawl_parallel(urls)
        else:
            self.logger.warning("No URLs found in sitemap.")

    async def _crawl_parallel(self, urls: List[str]):
        self.logger.info("Starting parallel crawling")
        browser_config = BrowserConfig(
            headless=True, 
            verbose=False, 
            extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"]
        )
        crawl_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)
        crawler = AsyncWebCrawler(config=browser_config)
        await crawler.start()

        try:
            for i in range(0, len(urls), self.max_concurrent):
                batch = urls[i: i + self.max_concurrent]
                tasks = [crawler.arun(url=url, config=crawl_config, session_id=f"session_{i + j}") for j, url in enumerate(batch)]

                results = await asyncio.gather(*tasks, return_exceptions=True)

                for url, result in zip(batch, results):
                    if isinstance(result, Exception):
                        self.logger.error(f"Error occurred while crawling {url}: {result}")
                    elif result.success:
                        self.logger.info(f"Successfully crawled: {url}")
                        self._save_markdown(result.markdown, url)
                    else:
                        self.logger.error(f"Failed to crawl {url}: {result.error_message}")

        except Exception as e:
            self.logger.error(f"Error during parallel crawling: {e}")
        finally:
            await crawler.close()

    def _get_urls_from_sitemap(self, sitemap_url: str) -> List[str]:
        try:
            response = requests.get(sitemap_url, timeout=10)  # Set a timeout for production readiness
            response.raise_for_status()
            root = ElementTree.fromstring(response.content)
            namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            urls = [loc.text for loc in root.findall('.//ns:loc', namespace)]
            return urls
        except Exception as e:
            self.logger.error(f"Error fetching sitemap {sitemap_url}: {e}")
            return []

    def _save_markdown(self, markdown: str, url: str):
        try:
            parsed_url = urlparse(url)
            domain = parsed_url.netloc.replace('.', '_')
            safe_filename = re.sub(r'[^\w\-_\. ]', '_', parsed_url.path.strip('/'))
            if not safe_filename:
                safe_filename = 'index'
            filepath = os.path.join(self.output_dir, f"{domain}_{safe_filename}.md")
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(markdown)
            self.logger.info(f"Markdown saved to: {filepath}")
        except Exception as e:
            self.logger.error(f"Error saving markdown for URL {url}: {e}")

async def main():
    # sitemap_url = os.getenv("SITEMAP_URL", "https://docs.crawl4ai.com/sitemap.xml")
    # scraper = WebScraper(output_dir="web_scraper_output")
    # await scraper.scrape_from_sitemap(sitemap_url)

    urls = [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3"
    ]
    scraper = WebScraper(output_dir="web_scraper_output")
    await scraper.scrape_multiple(urls)

if __name__ == "__main__":
    asyncio.run(main())
import os
import re
import sys
import asyncio
import logging
import requests
from dotenv import load_dotenv
from typing import List, Dict
from urllib.parse import urlparse
from xml.etree import ElementTree
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from pymongo import MongoClient
import chromadb
import json

# Add this block to modify sys.path if the script is run directly
if __name__ == "__main__" and __package__ is None:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.core.config import get_settings

settings = get_settings()

class WebScraper:
    def __init__(self, output_dir: str = settings.SCRAPER_OUTPUT_DIR, max_concurrent: int = settings.SCRAPER_MAX_CONCURRENT):
        self.output_dir = output_dir
        self.max_concurrent = max_concurrent
        os.makedirs(self.output_dir, exist_ok=True)

        # Set up basic logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger('WebScraper')

        # Initialize list to store markdowns
        self.output = []

    async def scrape_urls(self, urls: List[str]):
        self.logger.info("Starting to scrape multiple URLs")
        await self._crawl_parallel(urls)

    async def scrape_website(self, website: str):
        if not website.startswith(('http://', 'https://')):
            website = 'http://' + website

        sitemap_url = website if website.endswith('/sitemap.xml') else f"{website.rstrip('/')}/sitemap.xml"
       
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
                        self._store_markdown(result.markdown, url)
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

    def _store_markdown(self, markdown: str, url: str):
        try:
            parsed_url = urlparse(url)
            domain = parsed_url.netloc
            filename = parsed_url.path
            if not filename:
                filename = 'index'
            markdown_obj = {
                "url": url,
                "domain": domain,
                "filename": filename,
                "data": markdown
            }
            self.output.append(markdown_obj)
            self.logger.info(f"Markdown stored for URL: {url}")
        except Exception as e:
            self.logger.error(f"Error storing markdown for URL {url}: {e}")

async def main():
    scraper = WebScraper(output_dir="web_scraper_output")

    website = "www.themangojelly.com"
    await scraper.scrape_website(website)

    # urls = [
    #     "https://themangojelly.com/newsroom"
    # ]
    # await scraper.scrape_urls(urls)

    output_file = os.path.join(scraper.output_dir, "scraped_data.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(scraper.output, f, ensure_ascii=False, indent=4)
    scraper.logger.info(f"Markdowns saved to {output_file}")

if __name__ == "__main__":
    asyncio.run(main())
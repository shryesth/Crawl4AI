import asyncio
from crawl4ai import *

async def main():
    browser_config = BrowserConfig(
        headless=True,
        # For better performance in Docker or low-memory environments:
        extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
    )

    async with AsyncWebCrawler(config = browser_config) as crawler:
        url = "https://factset.sharepoint.com/:u:/r/sites/DataSolutionsPM/SitePages/Overview-of-Usage-%26-Metering.aspx?csf=1&web=1&e=qeoIFF"
        result = await crawler.arun(url = url)
        with open('output.md', 'w', encoding='utf-8') as file:
            file.write(result.markdown)
        print("Markdown content saved to output.md")

if __name__ == '__main__':
    asyncio.run(main())
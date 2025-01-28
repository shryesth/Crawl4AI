import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

async def scrape_with_edge_profile(url):
    # Specify the profile directory if needed.
    profile_dir = r"C:\Users\fds44813\AppData\Local\Microsoft\Edge\User Data\Default"
    
    # Browser configuration for crawling
    browser_config = BrowserConfig(
        headless=False,  # Set to True for no-browser interface
        use_managed_browser=True,
        browser_type="chromium",
        # user_data_dir=profile_dir,  # Since Edge is Chromium-based
        verbose=True,
    )
    
    # Configuring the crawler to wait 5 seconds before scraping
    crawler_run_config = CrawlerRunConfig(
        delay_before_return_html=5000  # Delay 5 seconds to let the page fully load
    )
    
    async with AsyncWebCrawler(config = browser_config) as crawler:
        # Execute the asynchronous crawl
        result = await crawler.arun(url=url, config=crawler_run_config)
        
        if result.success:
            print(result.markdown)
        else:
            print("Failed to crawl the page. Error:", result.error_message)

async def main():
    url = "https://factset.sharepoint.com/:u:/r/sites/DataSolutionsPM/SitePages/Overview-of-Usage-%26-Metering.aspx?csf=1&web=1&e=noJeDq"
    await scrape_with_edge_profile(url)

if __name__ == "__main__":
    # Run the asynchronous main function
    asyncio.run(main())

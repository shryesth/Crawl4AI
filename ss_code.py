import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

async def scrape_with_login(url):
    profile_dir = r"C:\Users\fds44813\AppData\Local\Microsoft\Edge\User Data\Default"
    
    browser_config = BrowserConfig(
        headless=False,  # False to see the browser window during debugging
        use_managed_browser=True,
        browser_type="chromium"
    )

    # JavaScript code to wait for a specific condition
    js_wait_for_page = """
    return new Promise((resolve) => {
        const check = () => {
            const element = document.querySelector('selector-for-confirmation'); // Change this to a valid selector
            if (element) {
                resolve(true);
            } else {
                setTimeout(check, 1000);  // Check every second
            }
        };
        check();
    });
    """

    async def on_page_context_created(crawler, page):
        # Wait for the page to be fully loaded and log in
        await page.evaluate(js_wait_for_page)

    # Configure the crawler run with the hook
    crawler_config = CrawlerRunConfig(
        hooks={
            'on_page_context_created': on_page_context_created
        }
    )
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url=url, config=crawler_config)

        if result.success:
            print("Successfully crawled the content after login")
            print(result.markdown)
        else:
            print("Failed to crawl the page:", result.error_message)

async def main():
    url = "https://factset.sharepoint.com/:u:/r/sites/DataSolutionsPM/SitePages/Overview-of-Usage-%26-Metering.aspx?csf=1&web=1&e=noJeDq"
    await scrape_with_login(url)

if __name__ == "__main__":
    asyncio.run(main())

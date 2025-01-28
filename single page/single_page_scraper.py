import asyncio
import random
import time
from crawl4ai import AsyncWebCrawler, BrowserConfig

async def main():
    browser_config = BrowserConfig(
        headless=False,
        user_data_dir="../my_chrome_profile",
        extra_args=[
            "--disable-gpu",
            "--disable-dev-shm-usage",
            "--no-sandbox",
            "--disable-blink-features=AutomationControlled"
        ],
    )
    
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"
    ]

    async with AsyncWebCrawler(config=browser_config) as crawler:
        crawler.crawler_strategy.set_custom_headers({
            "User-Agent": random.choice(user_agents),
            "Accept-Language": "en-US,en;q=0.9",
        })

        url = "https://www.linkedin.com/company/themangojelly/about/"
        
        time.sleep(random.uniform(3, 10))  # simulate human behavior
        
        result = await crawler.arun(url=url)
        
        if result.success:
            with open('output.md', 'w', encoding='utf-8') as file:
                file.write(result.markdown)
            print("Markdown content saved to output.md")
        else:
            print("Failed to retrieve content:", result.error_message)

if __name__ == '__main__':
    asyncio.run(main())

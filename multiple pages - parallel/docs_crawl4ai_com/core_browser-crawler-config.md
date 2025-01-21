[Crawl4AI Documentation](https://docs.crawl4ai.com/core/browser-crawler-config/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/core/browser-crawler-config/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/core/browser-crawler-config/<../quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/core/browser-crawler-config/<#>)


  * [Home](https://docs.crawl4ai.com/core/browser-crawler-config/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/browser-crawler-config/<../installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/core/browser-crawler-config/<../docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/core/browser-crawler-config/<../quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/core/browser-crawler-config/blog/>)
    * [Changelog](https://docs.crawl4ai.com/core/browser-crawler-config/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/core/browser-crawler-config/<../simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/core/browser-crawler-config/<../crawler-result/>)
    * Browser & Crawler Config
    * [Markdown Generation](https://docs.crawl4ai.com/core/browser-crawler-config/<../markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/core/browser-crawler-config/<../fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/core/browser-crawler-config/<../page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/core/browser-crawler-config/<../content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/core/browser-crawler-config/<../cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/browser-crawler-config/<../local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/core/browser-crawler-config/<../link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/core/browser-crawler-config/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/core/browser-crawler-config/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/core/browser-crawler-config/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/core/browser-crawler-config/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/core/browser-crawler-config/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/core/browser-crawler-config/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/core/browser-crawler-config/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/core/browser-crawler-config/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/core/browser-crawler-config/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/core/browser-crawler-config/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/core/browser-crawler-config/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/core/browser-crawler-config/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/core/browser-crawler-config/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/core/browser-crawler-config/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/core/browser-crawler-config/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/core/browser-crawler-config/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/browser-crawler-config/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/core/browser-crawler-config/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/core/browser-crawler-config/api/strategies/>)


  * [Browser & Crawler Configuration (Quick Overview)](https://docs.crawl4ai.com/core/browser-crawler-config/<#browser-crawler-configuration-quick-overview>)
  * [1. BrowserConfig Essentials](https://docs.crawl4ai.com/core/browser-crawler-config/<#1-browserconfig-essentials>)
  * [2. CrawlerRunConfig Essentials](https://docs.crawl4ai.com/core/browser-crawler-config/<#2-crawlerrunconfig-essentials>)
  * [3. Putting It All Together](https://docs.crawl4ai.com/core/browser-crawler-config/<#3-putting-it-all-together>)
  * [4. Next Steps](https://docs.crawl4ai.com/core/browser-crawler-config/<#4-next-steps>)
  * [5. Conclusion](https://docs.crawl4ai.com/core/browser-crawler-config/<#5-conclusion>)


# Browser & Crawler Configuration (Quick Overview)
Crawl4AI’s flexibility stems from two key classes:
1. **`BrowserConfig`**– Dictates**how** the browser is launched and behaves (e.g., headless or visible, proxy, user agent). 2. **`CrawlerRunConfig`**– Dictates**how** each **crawl** operates (e.g., caching, extraction, timeouts, JavaScript code to run, etc.).
In most examples, you create **one** `BrowserConfig` for the entire crawler session, then pass a **fresh** or re-used `CrawlerRunConfig` whenever you call `arun()`. This tutorial shows the most commonly used parameters. If you need advanced or rarely used fields, see the [Configuration Parameters](https://docs.crawl4ai.com/core/browser-crawler-config/api/parameters/>).
## 1. BrowserConfig Essentials
```
class BrowserConfig:
  def __init__(
    browser_type="chromium",
    headless=True,
    proxy_config=None,
    viewport_width=1080,
    viewport_height=600,
    verbose=True,
    use_persistent_context=False,
    user_data_dir=None,
    cookies=None,
    headers=None,
    user_agent=None,
    text_mode=False,
    light_mode=False,
    extra_args=None,
    # ... other advanced parameters omitted here
  ):
    ...

```

### Key Fields to Note
1. **`browser_type`**- Options:`"chromium"` , `"firefox"`, or `"webkit"`. - Defaults to `"chromium"`. - If you need a different engine, specify it here.
2. **`headless`**-`True` : Runs the browser in headless mode (invisible browser). - `False`: Runs the browser in visible mode, which helps with debugging.
3. **`proxy_config`**- A dictionary with fields like:
```
{
  "server": "http://proxy.example.com:8080", 
  "username": "...", 
  "password": "..."
}

```

- Leave as `None` if a proxy is not required. 
4. **`viewport_width` & `viewport_height`**: - The initial window size. - Some sites behave differently with smaller or bigger viewports.
5. **`verbose`**: - If`True` , prints extra logs. - Handy for debugging.
6. **`use_persistent_context`**: - If`True` , uses a **persistent** browser profile, storing cookies/local storage across runs. - Typically also set `user_data_dir` to point to a folder.
7. **`cookies`** & **`headers`**: - If you want to start with specific cookies or add universal HTTP headers, set them here. - E.g.`cookies=[{"name": "session", "value": "abc123", "domain": "example.com"}]`.
8. **`user_agent`**: - Custom User-Agent string. If`None` , a default is used. - You can also set `user_agent_mode="random"` for randomization (if you want to fight bot detection).
9. **`text_mode`** & **`light_mode`**: -`text_mode=True` disables images, possibly speeding up text-only crawls. - `light_mode=True` turns off certain background features for performance. 
10. **`extra_args`**: - Additional flags for the underlying browser. - E.g.`["--disable-extensions"]`.
**Minimal Example** :
```
from crawl4ai import AsyncWebCrawler, BrowserConfig
browser_conf = BrowserConfig(
  browser_type="firefox",
  headless=False,
  text_mode=True
)
async with AsyncWebCrawler(config=browser_conf) as crawler:
  result = await crawler.arun("https://example.com")
  print(result.markdown[:300])

```

## 2. CrawlerRunConfig Essentials
```
class CrawlerRunConfig:
  def __init__(
    word_count_threshold=200,
    extraction_strategy=None,
    markdown_generator=None,
    cache_mode=None,
    js_code=None,
    wait_for=None,
    screenshot=False,
    pdf=False,
    verbose=True,
    # ... other advanced parameters omitted
  ):
    ...

```

### Key Fields to Note
1. **`word_count_threshold`**: - The minimum word count before a block is considered. - If your site has lots of short paragraphs or items, you can lower it.
2. **`extraction_strategy`**: - Where you plug in JSON-based extraction (CSS, LLM, etc.). - If`None` , no structured extraction is done (only raw/cleaned HTML + markdown).
3. **`markdown_generator`**: - E.g.,`DefaultMarkdownGenerator(...)` , controlling how HTML→Markdown conversion is done. - If `None`, a default approach is used.
4. **`cache_mode`**: - Controls caching behavior (`ENABLED` , `BYPASS`, `DISABLED`, etc.). - If `None`, defaults to some level of caching or you can specify `CacheMode.ENABLED`.
5. **`js_code`**: - A string or list of JS strings to execute. - Great for “Load More” buttons or user interactions.
6. **`wait_for`**: - A CSS or JS expression to wait for before extracting content. - Common usage:`wait_for="css:.main-loaded"` or `wait_for="js:() => window.loaded === true"`.
7. **`screenshot`** & **`pdf`**: - If`True` , captures a screenshot or PDF after the page is fully loaded. - The results go to `result.screenshot` (base64) or `result.pdf` (bytes).
8. **`verbose`**: - Logs additional runtime details. - Overlaps with the browser’s verbosity if also set to`True` in `BrowserConfig`.
**Minimal Example** :
```
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
crawl_conf = CrawlerRunConfig(
  js_code="document.querySelector('button#loadMore')?.click()",
  wait_for="css:.loaded-content",
  screenshot=True
)
async with AsyncWebCrawler() as crawler:
  result = await crawler.arun(url="https://example.com", config=crawl_conf)
  print(result.screenshot[:100]) # Base64-encoded PNG snippet

```

## 3. Putting It All Together
In a typical scenario, you define **one** `BrowserConfig` for your crawler session, then create **one or more** `CrawlerRunConfig` depending on each call’s needs:
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def main():
  # 1) Browser config: headless, bigger viewport, no proxy
  browser_conf = BrowserConfig(
    headless=True,
    viewport_width=1280,
    viewport_height=720
  )
  # 2) Example extraction strategy
  schema = {
    "name": "Articles",
    "baseSelector": "div.article",
    "fields": [
      {"name": "title", "selector": "h2", "type": "text"},
      {"name": "link", "selector": "a", "type": "attribute", "attribute": "href"}
    ]
  }
  extraction = JsonCssExtractionStrategy(schema)
  # 3) Crawler run config: skip cache, use extraction
  run_conf = CrawlerRunConfig(
    extraction_strategy=extraction,
    cache_mode=CacheMode.BYPASS
  )
  async with AsyncWebCrawler(config=browser_conf) as crawler:
    # 4) Execute the crawl
    result = await crawler.arun(url="https://example.com/news", config=run_conf)
    if result.success:
      print("Extracted content:", result.extracted_content)
    else:
      print("Error:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

## 4. Next Steps
For a **detailed list** of available parameters (including advanced ones), see:
  * [BrowserConfig and CrawlerRunConfig Reference](https://docs.crawl4ai.com/core/browser-crawler-config/api/parameters/>)


You can explore topics like:
  * **Custom Hooks & Auth** (Inject JavaScript or handle login forms). 
  * **Session Management** (Re-use pages, preserve state across multiple calls). 
  * **Magic Mode** or **Identity-based Crawling** (Fight bot detection by simulating user behavior). 
  * **Advanced Caching** (Fine-tune read/write cache modes). 


## 5. Conclusion
**BrowserConfig** and **CrawlerRunConfig** give you straightforward ways to define:
  * **Which** browser to launch, how it should run, and any proxy or user agent needs. 
  * **How** each crawl should behave—caching, timeouts, JavaScript code, extraction strategies, etc.


Use them together for **clear, maintainable** code, and when you need more specialized behavior, check out the advanced parameters in the [reference docs](https://docs.crawl4ai.com/core/browser-crawler-config/api/parameters/>). Happy crawling!
Site built with [MkDocs](https://docs.crawl4ai.com/core/browser-crawler-config/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/core/browser-crawler-config/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching

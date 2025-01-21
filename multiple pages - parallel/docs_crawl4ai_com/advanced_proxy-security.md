[Crawl4AI Documentation](https://docs.crawl4ai.com/advanced/proxy-security/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/advanced/proxy-security/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/advanced/proxy-security/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/advanced/proxy-security/<#>)


  * [Home](https://docs.crawl4ai.com/advanced/proxy-security/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/advanced/proxy-security/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/advanced/proxy-security/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/advanced/proxy-security/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/advanced/proxy-security/blog/>)
    * [Changelog](https://docs.crawl4ai.com/advanced/proxy-security/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/advanced/proxy-security/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/advanced/proxy-security/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/proxy-security/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/advanced/proxy-security/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/advanced/proxy-security/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/advanced/proxy-security/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/advanced/proxy-security/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/advanced/proxy-security/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/advanced/proxy-security/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/advanced/proxy-security/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/proxy-security/<../advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/advanced/proxy-security/<../file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/proxy-security/<../lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/proxy-security/<../hooks-auth/>)
    * Proxy & Security
    * [Session Management](https://docs.crawl4ai.com/advanced/proxy-security/<../session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/proxy-security/<../multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/proxy-security/<../crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/proxy-security/<../identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/proxy-security/<../ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/advanced/proxy-security/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/advanced/proxy-security/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/advanced/proxy-security/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/advanced/proxy-security/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/advanced/proxy-security/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/advanced/proxy-security/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/proxy-security/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/advanced/proxy-security/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/advanced/proxy-security/api/strategies/>)


  * [Proxy](https://docs.crawl4ai.com/advanced/proxy-security/<#proxy>)
  * [Basic Proxy Setup](https://docs.crawl4ai.com/advanced/proxy-security/<#basic-proxy-setup>)
  * [Authenticated Proxy](https://docs.crawl4ai.com/advanced/proxy-security/<#authenticated-proxy>)
  * [Rotating Proxies](https://docs.crawl4ai.com/advanced/proxy-security/<#rotating-proxies>)


# Proxy
## Basic Proxy Setup
Simple proxy configuration with `BrowserConfig`:
```
from crawl4ai.async_configs import BrowserConfig
# Using proxy URL
browser_config = BrowserConfig(proxy="http://proxy.example.com:8080")
async with AsyncWebCrawler(config=browser_config) as crawler:
  result = await crawler.arun(url="https://example.com")
# Using SOCKS proxy
browser_config = BrowserConfig(proxy="socks5://proxy.example.com:1080")
async with AsyncWebCrawler(config=browser_config) as crawler:
  result = await crawler.arun(url="https://example.com")

```

## Authenticated Proxy
Use an authenticated proxy with `BrowserConfig`:
```
from crawl4ai.async_configs import BrowserConfig
proxy_config = {
  "server": "http://proxy.example.com:8080",
  "username": "user",
  "password": "pass"
}
browser_config = BrowserConfig(proxy_config=proxy_config)
async with AsyncWebCrawler(config=browser_config) as crawler:
  result = await crawler.arun(url="https://example.com")

```

## Rotating Proxies
Example using a proxy rotation service and updating `BrowserConfig` dynamically:
```
from crawl4ai.async_configs import BrowserConfig
async def get_next_proxy():
  # Your proxy rotation logic here
  return {"server": "http://next.proxy.com:8080"}
browser_config = BrowserConfig()
async with AsyncWebCrawler(config=browser_config) as crawler:
  # Update proxy for each request
  for url in urls:
    proxy = await get_next_proxy()
    browser_config.proxy_config = proxy
    result = await crawler.arun(url=url, config=browser_config)

```

Site built with [MkDocs](https://docs.crawl4ai.com/advanced/proxy-security/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/advanced/proxy-security/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching

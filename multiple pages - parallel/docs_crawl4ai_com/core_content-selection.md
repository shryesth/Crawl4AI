[Crawl4AI Documentation](https://docs.crawl4ai.com/core/content-selection/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/core/content-selection/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/core/content-selection/<../quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/core/content-selection/<#>)


  * [Home](https://docs.crawl4ai.com/core/content-selection/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/content-selection/<../installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/core/content-selection/<../docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/core/content-selection/<../quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/core/content-selection/blog/>)
    * [Changelog](https://docs.crawl4ai.com/core/content-selection/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/core/content-selection/<../simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/core/content-selection/<../crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/content-selection/<../browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/core/content-selection/<../markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/core/content-selection/<../fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/core/content-selection/<../page-interaction/>)
    * Content Selection
    * [Cache Modes](https://docs.crawl4ai.com/core/content-selection/<../cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/content-selection/<../local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/core/content-selection/<../link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/core/content-selection/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/core/content-selection/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/core/content-selection/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/core/content-selection/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/core/content-selection/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/core/content-selection/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/core/content-selection/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/core/content-selection/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/core/content-selection/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/core/content-selection/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/core/content-selection/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/core/content-selection/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/core/content-selection/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/core/content-selection/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/core/content-selection/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/core/content-selection/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/content-selection/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/core/content-selection/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/core/content-selection/api/strategies/>)


  * [Content Selection](https://docs.crawl4ai.com/core/content-selection/<#content-selection>)
  * [1. CSS-Based Selection](https://docs.crawl4ai.com/core/content-selection/<#1-css-based-selection>)
  * [2. Content Filtering & Exclusions](https://docs.crawl4ai.com/core/content-selection/<#2-content-filtering-exclusions>)
  * [3. Handling Iframes](https://docs.crawl4ai.com/core/content-selection/<#3-handling-iframes>)
  * [4. Structured Extraction Examples](https://docs.crawl4ai.com/core/content-selection/<#4-structured-extraction-examples>)
  * [5. Comprehensive Example](https://docs.crawl4ai.com/core/content-selection/<#5-comprehensive-example>)
  * [6. Conclusion](https://docs.crawl4ai.com/core/content-selection/<#6-conclusion>)


# Content Selection
Crawl4AI provides multiple ways to **select** , **filter** , and **refine** the content from your crawls. Whether you need to target a specific CSS region, exclude entire tags, filter out external links, or remove certain domains and images, **`CrawlerRunConfig`**offers a wide range of parameters.
Below, we show how to configure these parameters and combine them for precise control.
## 1. CSS-Based Selection
A straightforward way to **limit** your crawl results to a certain region of the page is **`css_selector`**in**`CrawlerRunConfig`**:
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
async def main():
  config = CrawlerRunConfig(
    # e.g., first 30 items from Hacker News
    css_selector=".athing:nth-child(-n+30)" 
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://news.ycombinator.com/newest", 
      config=config
    )
    print("Partial HTML length:", len(result.cleaned_html))
if __name__ == "__main__":
  asyncio.run(main())

```

**Result** : Only elements matching that selector remain in `result.cleaned_html`.
## 2. Content Filtering & Exclusions
### 2.1 Basic Overview
```
config = CrawlerRunConfig(
  # Content thresholds
  word_count_threshold=10,    # Minimum words per block
  # Tag exclusions
  excluded_tags=['form', 'header', 'footer', 'nav'],
  # Link filtering
  exclude_external_links=True,  
  exclude_social_media_links=True,
  # Block entire domains
  exclude_domains=["adtrackers.com", "spammynews.org"],  
  exclude_social_media_domains=["facebook.com", "twitter.com"],
  # Media filtering
  exclude_external_images=True
)

```

**Explanation** :
  * **`word_count_threshold`**: Ignores text blocks under X words. Helps skip trivial blocks like short nav or disclaimers.
  * **`excluded_tags`**: Removes entire tags (`<form>` , `<header>`, `<footer>`, etc.). 
  * **Link Filtering** : 
  * `exclude_external_links`: Strips out external links and may remove them from `result.links`. 
  * `exclude_social_media_links`: Removes links pointing to known social media domains. 
  * `exclude_domains`: A custom list of domains to block if discovered in links. 
  * `exclude_social_media_domains`: A curated list (override or add to it) for social media sites. 
  * **Media Filtering** : 
  * `exclude_external_images`: Discards images not hosted on the same domain as the main page (or its subdomains).


By default in case you set `exclude_social_media_links=True`, the following social media domains are excluded: 
```
[
  'facebook.com',
  'twitter.com',
  'x.com',
  'linkedin.com',
  'instagram.com',
  'pinterest.com',
  'tiktok.com',
  'snapchat.com',
  'reddit.com',
]

```

### 2.2 Example Usage
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
async def main():
  config = CrawlerRunConfig(
    css_selector="main.content", 
    word_count_threshold=10,
    excluded_tags=["nav", "footer"],
    exclude_external_links=True,
    exclude_social_media_links=True,
    exclude_domains=["ads.com", "spammytrackers.net"],
    exclude_external_images=True,
    cache_mode=CacheMode.BYPASS
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url="https://news.ycombinator.com", config=config)
    print("Cleaned HTML length:", len(result.cleaned_html))
if __name__ == "__main__":
  asyncio.run(main())

```

**Note** : If these parameters remove too much, reduce or disable them accordingly.
## 3. Handling Iframes
Some sites embed content in `<iframe>` tags. If you want that inline: 
```
config = CrawlerRunConfig(
  # Merge iframe content into the final output
  process_iframes=True,  
  remove_overlay_elements=True
)

```

**Usage** : 
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
async def main():
  config = CrawlerRunConfig(
    process_iframes=True,
    remove_overlay_elements=True
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://example.org/iframe-demo", 
      config=config
    )
    print("Iframe-merged length:", len(result.cleaned_html))
if __name__ == "__main__":
  asyncio.run(main())

```

## 4. Structured Extraction Examples
You can combine content selection with a more advanced extraction strategy. For instance, a **CSS-based** or **LLM-based** extraction strategy can run on the filtered HTML.
### 4.1 Pattern-Based with `JsonCssExtractionStrategy`
```
import asyncio
import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def main():
  # Minimal schema for repeated items
  schema = {
    "name": "News Items",
    "baseSelector": "tr.athing",
    "fields": [
      {"name": "title", "selector": "a.storylink", "type": "text"},
      {
        "name": "link", 
        "selector": "a.storylink", 
        "type": "attribute", 
        "attribute": "href"
      }
    ]
  }
  config = CrawlerRunConfig(
    # Content filtering
    excluded_tags=["form", "header"],
    exclude_domains=["adsite.com"],
    # CSS selection or entire page
    css_selector="table.itemlist",
    # No caching for demonstration
    cache_mode=CacheMode.BYPASS,
    # Extraction strategy
    extraction_strategy=JsonCssExtractionStrategy(schema)
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://news.ycombinator.com/newest", 
      config=config
    )
    data = json.loads(result.extracted_content)
    print("Sample extracted item:", data[:1]) # Show first item
if __name__ == "__main__":
  asyncio.run(main())

```

### 4.2 LLM-Based Extraction
```
import asyncio
import json
from pydantic import BaseModel, Field
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy
class ArticleData(BaseModel):
  headline: str
  summary: str
async def main():
  llm_strategy = LLMExtractionStrategy(
    provider="openai/gpt-4",
    api_token="sk-YOUR_API_KEY",
    schema=ArticleData.schema(),
    extraction_type="schema",
    instruction="Extract 'headline' and a short 'summary' from the content."
  )
  config = CrawlerRunConfig(
    exclude_external_links=True,
    word_count_threshold=20,
    extraction_strategy=llm_strategy
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url="https://news.ycombinator.com", config=config)
    article = json.loads(result.extracted_content)
    print(article)
if __name__ == "__main__":
  asyncio.run(main())

```

Here, the crawler:
  * Filters out external links (`exclude_external_links=True`). 
  * Ignores very short text blocks (`word_count_threshold=20`). 
  * Passes the final HTML to your LLM strategy for an AI-driven parse.


## 5. Comprehensive Example
Below is a short function that unifies **CSS selection** , **exclusion** logic, and a pattern-based extraction, demonstrating how you can fine-tune your final data:
```
import asyncio
import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def extract_main_articles(url: str):
  schema = {
    "name": "ArticleBlock",
    "baseSelector": "div.article-block",
    "fields": [
      {"name": "headline", "selector": "h2", "type": "text"},
      {"name": "summary", "selector": ".summary", "type": "text"},
      {
        "name": "metadata",
        "type": "nested",
        "fields": [
          {"name": "author", "selector": ".author", "type": "text"},
          {"name": "date", "selector": ".date", "type": "text"}
        ]
      }
    ]
  }
  config = CrawlerRunConfig(
    # Keep only #main-content
    css_selector="#main-content",
    # Filtering
    word_count_threshold=10,
    excluded_tags=["nav", "footer"], 
    exclude_external_links=True,
    exclude_domains=["somebadsite.com"],
    exclude_external_images=True,
    # Extraction
    extraction_strategy=JsonCssExtractionStrategy(schema),
    cache_mode=CacheMode.BYPASS
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url=url, config=config)
    if not result.success:
      print(f"Error: {result.error_message}")
      return None
    return json.loads(result.extracted_content)
async def main():
  articles = await extract_main_articles("https://news.ycombinator.com/newest")
  if articles:
    print("Extracted Articles:", articles[:2]) # Show first 2
if __name__ == "__main__":
  asyncio.run(main())

```

**Why This Works** : - **CSS** scoping with `#main-content`. - Multiple **exclude_** parameters to remove domains, external images, etc. - A **JsonCssExtractionStrategy** to parse repeated article blocks.
## 6. Conclusion
By mixing **css_selector** scoping, **content filtering** parameters, and advanced **extraction strategies** , you can precisely **choose** which data to keep. Key parameters in **`CrawlerRunConfig`**for content selection include:
1. **`css_selector`**– Basic scoping to an element or region. 2.**`word_count_threshold`**– Skip short blocks. 3.**`excluded_tags`**– Remove entire HTML tags. 4.**`exclude_external_links`**,**`exclude_social_media_links`**,**`exclude_domains`**– Filter out unwanted links or domains. 5.**`exclude_external_images`**– Remove images from external sources. 6.**`process_iframes`**– Merge iframe content if needed.
Combine these with structured extraction (CSS, LLM-based, or others) to build powerful crawls that yield exactly the content you want, from raw or cleaned HTML up to sophisticated JSON structures. For more detail, see [Configuration Reference](https://docs.crawl4ai.com/core/content-selection/api/parameters/>). Enjoy curating your data to the max!
Site built with [MkDocs](https://docs.crawl4ai.com/core/content-selection/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/core/content-selection/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching

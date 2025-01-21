[Crawl4AI Documentation](https://docs.crawl4ai.com/extraction/no-llm-strategies/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/extraction/no-llm-strategies/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/extraction/no-llm-strategies/<#>)


  * [Home](https://docs.crawl4ai.com/extraction/no-llm-strategies/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/extraction/no-llm-strategies/blog/>)
    * [Changelog](https://docs.crawl4ai.com/extraction/no-llm-strategies/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/extraction/no-llm-strategies/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/extraction/no-llm-strategies/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/extraction/no-llm-strategies/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/extraction/no-llm-strategies/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/extraction/no-llm-strategies/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/extraction/no-llm-strategies/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/extraction/no-llm-strategies/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/extraction/no-llm-strategies/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/extraction/no-llm-strategies/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/extraction/no-llm-strategies/advanced/ssl-certificate/>)
  * Extraction
    * LLM-Free Strategies
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/<../llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/<../clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/extraction/no-llm-strategies/<../chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/extraction/no-llm-strategies/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/extraction/no-llm-strategies/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/extraction/no-llm-strategies/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/extraction/no-llm-strategies/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/api/strategies/>)


  * [Extracting JSON (No LLM)](https://docs.crawl4ai.com/extraction/no-llm-strategies/<#extracting-json-no-llm>)
  * [1. Intro to Schema-Based Extraction](https://docs.crawl4ai.com/extraction/no-llm-strategies/<#1-intro-to-schema-based-extraction>)
  * [2. Simple Example: Crypto Prices](https://docs.crawl4ai.com/extraction/no-llm-strategies/<#2-simple-example-crypto-prices>)
  * [3. Advanced Schema & Nested Structures](https://docs.crawl4ai.com/extraction/no-llm-strategies/<#3-advanced-schema-nested-structures>)
  * [4. Why “No LLM” Is Often Better](https://docs.crawl4ai.com/extraction/no-llm-strategies/<#4-why-no-llm-is-often-better>)
  * [5. Base Element Attributes & Additional Fields](https://docs.crawl4ai.com/extraction/no-llm-strategies/<#5-base-element-attributes-additional-fields>)
  * [6. Putting It All Together: Larger Example](https://docs.crawl4ai.com/extraction/no-llm-strategies/<#6-putting-it-all-together-larger-example>)
  * [7. Tips & Best Practices](https://docs.crawl4ai.com/extraction/no-llm-strategies/<#7-tips-best-practices>)
  * [8. Conclusion](https://docs.crawl4ai.com/extraction/no-llm-strategies/<#8-conclusion>)


# Extracting JSON (No LLM)
One of Crawl4AI’s **most powerful** features is extracting **structured JSON** from websites **without** relying on large language models. By defining a **schema** with CSS or XPath selectors, you can extract data instantly—even from complex or nested HTML structures—without the cost, latency, or environmental impact of an LLM.
**Why avoid LLM for basic extractions?**
1. **Faster & Cheaper**: No API calls or GPU overhead. 2. **Lower Carbon Footprint** : LLM inference can be energy-intensive. A well-defined schema is practically carbon-free. 3. **Precise & Repeatable**: CSS/XPath selectors do exactly what you specify. LLM outputs can vary or hallucinate. 4. **Scales Readily** : For thousands of pages, schema-based extraction runs quickly and in parallel.
Below, we’ll explore how to craft these schemas and use them with **JsonCssExtractionStrategy** (or **JsonXPathExtractionStrategy** if you prefer XPath). We’ll also highlight advanced features like **nested fields** and **base element attributes**.
## 1. Intro to Schema-Based Extraction
A schema defines:
  1. A **base selector** that identifies each “container” element on the page (e.g., a product row, a blog post card). 2. **Fields** describing which CSS/XPath selectors to use for each piece of data you want to capture (text, attribute, HTML block, etc.). 3. **Nested** or **list** types for repeated or hierarchical structures. 


For example, if you have a list of products, each one might have a name, price, reviews, and “related products.” This approach is faster and more reliable than an LLM for consistent, structured pages.
## 2. Simple Example: Crypto Prices
Let’s begin with a **simple** schema-based extraction using the `JsonCssExtractionStrategy`. Below is a snippet that extracts cryptocurrency prices from a site (similar to the legacy Coinbase example). Notice we **don’t** call any LLM:
```
import json
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def extract_crypto_prices():
  # 1. Define a simple extraction schema
  schema = {
    "name": "Crypto Prices",
    "baseSelector": "div.crypto-row",  # Repeated elements
    "fields": [
      {
        "name": "coin_name",
        "selector": "h2.coin-name",
        "type": "text"
      },
      {
        "name": "price",
        "selector": "span.coin-price",
        "type": "text"
      }
    ]
  }
  # 2. Create the extraction strategy
  extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)
  # 3. Set up your crawler config (if needed)
  config = CrawlerRunConfig(
    # e.g., pass js_code or wait_for if the page is dynamic
    # wait_for="css:.crypto-row:nth-child(20)"
    cache_mode = CacheMode.BYPASS,
    extraction_strategy=extraction_strategy,
  )
  async with AsyncWebCrawler(verbose=True) as crawler:
    # 4. Run the crawl and extraction
    result = await crawler.arun(
      url="https://example.com/crypto-prices",
      config=config
    )
    if not result.success:
      print("Crawl failed:", result.error_message)
      return
    # 5. Parse the extracted JSON
    data = json.loads(result.extracted_content)
    print(f"Extracted {len(data)} coin entries")
    print(json.dumps(data[0], indent=2) if data else "No data found")
asyncio.run(extract_crypto_prices())

```

**Highlights** :
  * **`baseSelector`**: Tells us where each “item” (crypto row) is.
  * **`fields`**: Two fields (`coin_name` , `price`) using simple CSS selectors. 
  * Each field defines a **`type`**(e.g.,`text` , `attribute`, `html`, `regex`, etc.).


No LLM is needed, and the performance is **near-instant** for hundreds or thousands of items.
### **XPath Example with`raw://` HTML**
Below is a short example demonstrating **XPath** extraction plus the **`raw://`**scheme. We’ll pass a**dummy HTML** directly (no network request) and define the extraction strategy in `CrawlerRunConfig`.
```
import json
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.extraction_strategy import JsonXPathExtractionStrategy
async def extract_crypto_prices_xpath():
  # 1. Minimal dummy HTML with some repeating rows
  dummy_html = """
  <html>
   <body>
    <div class='crypto-row'>
     <h2 class='coin-name'>Bitcoin</h2>
     <span class='coin-price'>$28,000</span>
    </div>
    <div class='crypto-row'>
     <h2 class='coin-name'>Ethereum</h2>
     <span class='coin-price'>$1,800</span>
    </div>
   </body>
  </html>
  """
  # 2. Define the JSON schema (XPath version)
  schema = {
    "name": "Crypto Prices via XPath",
    "baseSelector": "//div[@class='crypto-row']",
    "fields": [
      {
        "name": "coin_name",
        "selector": ".//h2[@class='coin-name']",
        "type": "text"
      },
      {
        "name": "price",
        "selector": ".//span[@class='coin-price']",
        "type": "text"
      }
    ]
  }
  # 3. Place the strategy in the CrawlerRunConfig
  config = CrawlerRunConfig(
    extraction_strategy=JsonXPathExtractionStrategy(schema, verbose=True)
  )
  # 4. Use raw:// scheme to pass dummy_html directly
  raw_url = f"raw://{dummy_html}"
  async with AsyncWebCrawler(verbose=True) as crawler:
    result = await crawler.arun(
      url=raw_url,
      config=config
    )
    if not result.success:
      print("Crawl failed:", result.error_message)
      return
    data = json.loads(result.extracted_content)
    print(f"Extracted {len(data)} coin rows")
    if data:
      print("First item:", data[0])
asyncio.run(extract_crypto_prices_xpath())

```

**Key Points** :
1. **`JsonXPathExtractionStrategy`**is used instead of`JsonCssExtractionStrategy`. 2. **`baseSelector`**and each field’s`"selector"` use **XPath** instead of CSS. 3. **`raw://`**lets us pass`dummy_html` with no real network request—handy for local testing. 4. Everything (including the extraction strategy) is in **`CrawlerRunConfig`**.
That’s how you keep the config self-contained, illustrate **XPath** usage, and demonstrate the **raw** scheme for direct HTML input—all while avoiding the old approach of passing `extraction_strategy` directly to `arun()`.
## 3. Advanced Schema & Nested Structures
Real sites often have **nested** or repeated data—like categories containing products, which themselves have a list of reviews or features. For that, we can define **nested** or **list** (and even **nested_list**) fields.
### Sample E-Commerce HTML
We have a **sample e-commerce** HTML file on GitHub (example): 
```
https://gist.githubusercontent.com/githubusercontent/2d7b8ba3cd8ab6cf3c8da771ddb36878/raw/1ae2f90c6861ce7dd84cc50d3df9920dee5e1fd2/sample_ecommerce.html

```

This snippet includes categories, products, features, reviews, and related items. Let’s see how to define a schema that fully captures that structure **without LLM**. 
```
schema = {
  "name": "E-commerce Product Catalog",
  "baseSelector": "div.category",
  # (1) We can define optional baseFields if we want to extract attributes 
  # from the category container
  "baseFields": [
    {"name": "data_cat_id", "type": "attribute", "attribute": "data-cat-id"}, 
  ],
  "fields": [
    {
      "name": "category_name",
      "selector": "h2.category-name",
      "type": "text"
    },
    {
      "name": "products",
      "selector": "div.product",
      "type": "nested_list",  # repeated sub-objects
      "fields": [
        {
          "name": "name",
          "selector": "h3.product-name",
          "type": "text"
        },
        {
          "name": "price",
          "selector": "p.product-price",
          "type": "text"
        },
        {
          "name": "details",
          "selector": "div.product-details",
          "type": "nested", # single sub-object
          "fields": [
            {
              "name": "brand",
              "selector": "span.brand",
              "type": "text"
            },
            {
              "name": "model",
              "selector": "span.model",
              "type": "text"
            }
          ]
        },
        {
          "name": "features",
          "selector": "ul.product-features li",
          "type": "list",
          "fields": [
            {"name": "feature", "type": "text"} 
          ]
        },
        {
          "name": "reviews",
          "selector": "div.review",
          "type": "nested_list",
          "fields": [
            {
              "name": "reviewer", 
              "selector": "span.reviewer", 
              "type": "text"
            },
            {
              "name": "rating", 
              "selector": "span.rating", 
              "type": "text"
            },
            {
              "name": "comment", 
              "selector": "p.review-text", 
              "type": "text"
            }
          ]
        },
        {
          "name": "related_products",
          "selector": "ul.related-products li",
          "type": "list",
          "fields": [
            {
              "name": "name", 
              "selector": "span.related-name", 
              "type": "text"
            },
            {
              "name": "price", 
              "selector": "span.related-price", 
              "type": "text"
            }
          ]
        }
      ]
    }
  ]
}

```

Key Takeaways:
  * **Nested vs. List** : 
  * **`type: "nested"`**means a**single** sub-object (like `details`). 
  * **`type: "list"`**means multiple items that are**simple** dictionaries or single text fields. 
  * **`type: "nested_list"`**means repeated**complex** objects (like `products` or `reviews`).
  * **Base Fields** : We can extract **attributes** from the container element via `"baseFields"`. For instance, `"data_cat_id"` might be `data-cat-id="elect123"`. 
  * **Transforms** : We can also define a `transform` if we want to lower/upper case, strip whitespace, or even run a custom function.


### Running the Extraction
```
import json
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
ecommerce_schema = {
  # ... the advanced schema from above ...
}
async def extract_ecommerce_data():
  strategy = JsonCssExtractionStrategy(ecommerce_schema, verbose=True)
  config = CrawlerRunConfig()
  async with AsyncWebCrawler(verbose=True) as crawler:
    result = await crawler.arun(
      url="https://gist.githubusercontent.com/githubusercontent/2d7b8ba3cd8ab6cf3c8da771ddb36878/raw/1ae2f90c6861ce7dd84cc50d3df9920dee5e1fd2/sample_ecommerce.html",
      extraction_strategy=strategy,
      config=config
    )
    if not result.success:
      print("Crawl failed:", result.error_message)
      return
    # Parse the JSON output
    data = json.loads(result.extracted_content)
    print(json.dumps(data, indent=2) if data else "No data found.")
asyncio.run(extract_ecommerce_data())

```

If all goes well, you get a **structured** JSON array with each “category,” containing an array of `products`. Each product includes `details`, `features`, `reviews`, etc. All of that **without** an LLM.
## 4. Why “No LLM” Is Often Better
1. **Zero Hallucination** : Schema-based extraction doesn’t guess text. It either finds it or not. 2. **Guaranteed Structure** : The same schema yields consistent JSON across many pages, so your downstream pipeline can rely on stable keys. 3. **Speed** : LLM-based extraction can be 10–1000x slower for large-scale crawling. 4. **Scalable** : Adding or updating a field is a matter of adjusting the schema, not re-tuning a model.
**When might you consider an LLM?** Possibly if the site is extremely unstructured or you want AI summarization. But always try a schema approach first for repeated or consistent data patterns.
## 5. Base Element Attributes & Additional Fields
It’s easy to **extract attributes** (like `href`, `src`, or `data-xxx`) from your base or nested elements using:
```
{
 "name": "href",
 "type": "attribute",
 "attribute": "href",
 "default": null
}

```

You can define them in **`baseFields`**(extracted from the main container element) or in each field’s sub-lists. This is especially helpful if you need an item’s link or ID stored in the parent`<div>`.
## 6. Putting It All Together: Larger Example
Consider a blog site. We have a schema that extracts the **URL** from each post card (via `baseFields` with an `"attribute": "href"`), plus the title, date, summary, and author:
```
schema = {
 "name": "Blog Posts",
 "baseSelector": "a.blog-post-card",
 "baseFields": [
  {"name": "post_url", "type": "attribute", "attribute": "href"}
 ],
 "fields": [
  {"name": "title", "selector": "h2.post-title", "type": "text", "default": "No Title"},
  {"name": "date", "selector": "time.post-date", "type": "text", "default": ""},
  {"name": "summary", "selector": "p.post-summary", "type": "text", "default": ""},
  {"name": "author", "selector": "span.post-author", "type": "text", "default": ""}
 ]
}

```

Then run with `JsonCssExtractionStrategy(schema)` to get an array of blog post objects, each with `"post_url"`, `"title"`, `"date"`, `"summary"`, `"author"`.
## 7. Tips & Best Practices
1. **Inspect the DOM** in Chrome DevTools or Firefox’s Inspector to find stable selectors. 2. **Start Simple** : Verify you can extract a single field. Then add complexity like nested objects or lists. 3. **Test** your schema on partial HTML or a test page before a big crawl. 4. **Combine with JS Execution** if the site loads content dynamically. You can pass `js_code` or `wait_for` in `CrawlerRunConfig`. 5. **Look at Logs** when `verbose=True`: if your selectors are off or your schema is malformed, it’ll often show warnings. 6. **Use baseFields** if you need attributes from the container element (e.g., `href`, `data-id`), especially for the “parent” item. 7. **Performance** : For large pages, make sure your selectors are as narrow as possible.
## 8. Conclusion
With **JsonCssExtractionStrategy** (or **JsonXPathExtractionStrategy**), you can build powerful, **LLM-free** pipelines that:
  * Scrape any consistent site for structured data. 
  * Support nested objects, repeating lists, or advanced transformations. 
  * Scale to thousands of pages quickly and reliably.


**Next Steps** :
  * Combine your extracted JSON with advanced filtering or summarization in a second pass if needed. 
  * For dynamic pages, combine strategies with `js_code` or infinite scroll hooking to ensure all content is loaded.


**Remember** : For repeated, structured data, you don’t need to pay for or wait on an LLM. A well-crafted schema plus CSS or XPath gets you the data faster, cleaner, and cheaper—**the real power** of Crawl4AI.
**Last Updated** : 2025-01-01
That’s it for **Extracting JSON (No LLM)**! You’ve seen how schema-based approaches (either CSS or XPath) can handle everything from simple lists to deeply nested product catalogs—instantly, with minimal overhead. Enjoy building robust scrapers that produce consistent, structured JSON for your data pipelines!
Site built with [MkDocs](https://docs.crawl4ai.com/extraction/no-llm-strategies/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/extraction/no-llm-strategies/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching

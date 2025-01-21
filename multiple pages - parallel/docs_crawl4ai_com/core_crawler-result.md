[Crawl4AI Documentation](https://docs.crawl4ai.com/core/crawler-result/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/core/crawler-result/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/core/crawler-result/<../quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/core/crawler-result/<#>)


  * [Home](https://docs.crawl4ai.com/core/crawler-result/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/crawler-result/<../installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/core/crawler-result/<../docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/core/crawler-result/<../quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/core/crawler-result/blog/>)
    * [Changelog](https://docs.crawl4ai.com/core/crawler-result/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/core/crawler-result/<../simple-crawling/>)
    * Crawler Result
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/crawler-result/<../browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/core/crawler-result/<../markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/core/crawler-result/<../fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/core/crawler-result/<../page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/core/crawler-result/<../content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/core/crawler-result/<../cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/crawler-result/<../local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/core/crawler-result/<../link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/core/crawler-result/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/core/crawler-result/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/core/crawler-result/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/core/crawler-result/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/core/crawler-result/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/core/crawler-result/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/core/crawler-result/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/core/crawler-result/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/core/crawler-result/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/core/crawler-result/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/core/crawler-result/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/core/crawler-result/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/core/crawler-result/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/core/crawler-result/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/core/crawler-result/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/core/crawler-result/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/crawler-result/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/core/crawler-result/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/core/crawler-result/api/strategies/>)


  * [Crawl Result and Output](https://docs.crawl4ai.com/core/crawler-result/<#crawl-result-and-output>)
  * [1. The CrawlResult Model](https://docs.crawl4ai.com/core/crawler-result/<#1-the-crawlresult-model>)
  * [2. HTML Variants](https://docs.crawl4ai.com/core/crawler-result/<#2-html-variants>)
  * [3. Markdown Generation](https://docs.crawl4ai.com/core/crawler-result/<#3-markdown-generation>)
  * [4. Structured Extraction: extracted_content](https://docs.crawl4ai.com/core/crawler-result/<#4-structured-extraction-extracted_content>)
  * [5. More Fields: Links, Media, and More](https://docs.crawl4ai.com/core/crawler-result/<#5-more-fields-links-media-and-more>)
  * [6. Accessing These Fields](https://docs.crawl4ai.com/core/crawler-result/<#6-accessing-these-fields>)
  * [7. Next Steps](https://docs.crawl4ai.com/core/crawler-result/<#7-next-steps>)


# Crawl Result and Output
When you call `arun()` on a page, Crawl4AI returns a **`CrawlResult`**object containing everything you might need—raw HTML, a cleaned version, optional screenshots or PDFs, structured extraction results, and more. This document explains those fields and how they map to different output types.
## 1. The `CrawlResult` Model
Below is the core schema. Each field captures a different aspect of the crawl’s result:
```
class MarkdownGenerationResult(BaseModel):
  raw_markdown: str
  markdown_with_citations: str
  references_markdown: str
  fit_markdown: Optional[str] = None
  fit_html: Optional[str] = None
class CrawlResult(BaseModel):
  url: str
  html: str
  success: bool
  cleaned_html: Optional[str] = None
  media: Dict[str, List[Dict]] = {}
  links: Dict[str, List[Dict]] = {}
  downloaded_files: Optional[List[str]] = None
  screenshot: Optional[str] = None
  pdf : Optional[bytes] = None
  markdown: Optional[Union[str, MarkdownGenerationResult]] = None
  markdown_v2: Optional[MarkdownGenerationResult] = None
  extracted_content: Optional[str] = None
  metadata: Optional[dict] = None
  error_message: Optional[str] = None
  session_id: Optional[str] = None
  response_headers: Optional[dict] = None
  status_code: Optional[int] = None
  ssl_certificate: Optional[SSLCertificate] = None
  class Config:
    arbitrary_types_allowed = True

```

### Table: Key Fields in `CrawlResult`
Field (Name & Type) | Description  
---|---  
**url (`str`)** | The final or actual URL crawled (in case of redirects).  
**html (`str`)** | Original, unmodified page HTML. Good for debugging or custom processing.  
**success (`bool`)** | `True` if the crawl completed without major errors, else `False`.  
**cleaned_html (`Optional[str]`)** | Sanitized HTML with scripts/styles removed; can exclude tags if configured via `excluded_tags` etc.  
**media (`Dict[str, List[Dict]]`)** | Extracted media info (images, audio, etc.), each with attributes like `src`, `alt`, `score`, etc.  
**links (`Dict[str, List[Dict]]`)** | Extracted link data, split by `internal` and `external`. Each link usually has `href`, `text`, etc.  
**downloaded_files (`Optional[List[str]]`)** | If `accept_downloads=True` in `BrowserConfig`, this lists the filepaths of saved downloads.  
**screenshot (`Optional[str]`)** | Screenshot of the page (base64-encoded) if `screenshot=True`.  
**pdf (`Optional[bytes]`)** | PDF of the page if `pdf=True`.  
**markdown (`Optional[str or MarkdownGenerationResult]`)** | For now, `markdown_v2` holds a `MarkdownGenerationResult`. Over time, this will be consolidated into `markdown`. The generator can provide raw markdown, citations, references, and optionally `fit_markdown`.  
**markdown_v2 (`Optional[MarkdownGenerationResult]`)** | Legacy field for detailed markdown output. This will be replaced by `markdown` soon.  
**extracted_content (`Optional[str]`)** | The output of a structured extraction (CSS/LLM-based) stored as JSON string or other text.  
**metadata (`Optional[dict]`)** | Additional info about the crawl or extracted data.  
**error_message (`Optional[str]`)** | If `success=False`, contains a short description of what went wrong.  
**session_id (`Optional[str]`)** | The ID of the session used for multi-page or persistent crawling.  
**response_headers (`Optional[dict]`)** | HTTP response headers, if captured.  
**status_code (`Optional[int]`)** | HTTP status code (e.g., 200 for OK).  
**ssl_certificate (`Optional[SSLCertificate]`)** | SSL certificate info if `fetch_ssl_certificate=True`.  
## 2. HTML Variants
### `html`: Raw HTML
Crawl4AI preserves the exact HTML as `result.html`. Useful for:
  * Debugging page issues or checking the original content.
  * Performing your own specialized parse if needed.


### `cleaned_html`: Sanitized
If you specify any cleanup or exclusion parameters in `CrawlerRunConfig` (like `excluded_tags`, `remove_forms`, etc.), you’ll see the result here:
```
config = CrawlerRunConfig(
  excluded_tags=["form", "header", "footer"],
  keep_data_attributes=False
)
result = await crawler.arun("https://example.com", config=config)
print(result.cleaned_html) # Freed of forms, header, footer, data-* attributes

```

## 3. Markdown Generation
### 3.1 `markdown_v2` (Legacy) vs `markdown`
  * **`markdown_v2`**: The current location for detailed markdown output, returning a**`MarkdownGenerationResult`**object.
  * **`markdown`**: Eventually, we’re merging these fields. For now, you might see`result.markdown_v2` used widely in code examples.


**`MarkdownGenerationResult`**Fields:
Field | Description  
---|---  
**raw_markdown** | The basic HTML→Markdown conversion.  
**markdown_with_citations** | Markdown including inline citations that reference links at the end.  
**references_markdown** | The references/citations themselves (if `citations=True`).  
**fit_markdown** | The filtered/“fit” markdown if a content filter was used.  
**fit_html** | The filtered HTML that generated `fit_markdown`.  
### 3.2 Basic Example with a Markdown Generator
```
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
config = CrawlerRunConfig(
  markdown_generator=DefaultMarkdownGenerator(
    options={"citations": True, "body_width": 80} # e.g. pass html2text style options
  )
)
result = await crawler.arun(url="https://example.com", config=config)
md_res = result.markdown_v2 # or eventually 'result.markdown'
print(md_res.raw_markdown[:500])
print(md_res.markdown_with_citations)
print(md_res.references_markdown)

```

**Note** : If you use a filter like `PruningContentFilter`, you’ll get `fit_markdown` and `fit_html` as well.
## 4. Structured Extraction: `extracted_content`
If you run a JSON-based extraction strategy (CSS, XPath, LLM, etc.), the structured data is **not** stored in `markdown`—it’s placed in **`result.extracted_content`**as a JSON string (or sometimes plain text).
### Example: CSS Extraction with `raw://` HTML
```
import asyncio
import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def main():
  schema = {
    "name": "Example Items",
    "baseSelector": "div.item",
    "fields": [
      {"name": "title", "selector": "h2", "type": "text"},
      {"name": "link", "selector": "a", "type": "attribute", "attribute": "href"}
    ]
  }
  raw_html = "<div class='item'><h2>Item 1</h2><a href='https://example.com/item1'>Link 1</a></div>"
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="raw://" + raw_html,
      config=CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        extraction_strategy=JsonCssExtractionStrategy(schema)
      )
    )
    data = json.loads(result.extracted_content)
    print(data)
if __name__ == "__main__":
  asyncio.run(main())

```

Here: - `url="raw://..."` passes the HTML content directly, no network requests. - The **CSS** extraction strategy populates `result.extracted_content` with the JSON array `[{"title": "...", "link": "..."}]`.
## 5. More Fields: Links, Media, and More
### 5.1 `links`
A dictionary, typically with `"internal"` and `"external"` lists. Each entry might have `href`, `text`, `title`, etc. This is automatically captured if you haven’t disabled link extraction.
```
print(result.links["internal"][:3]) # Show first 3 internal links

```

### 5.2 `media`
Similarly, a dictionary with `"images"`, `"audio"`, `"video"`, etc. Each item could include `src`, `alt`, `score`, and more, if your crawler is set to gather them.
```
images = result.media.get("images", [])
for img in images:
  print("Image URL:", img["src"], "Alt:", img.get("alt"))

```

### 5.3 `screenshot` and `pdf`
If you set `screenshot=True` or `pdf=True` in **`CrawlerRunConfig`**, then:
  * `result.screenshot` contains a base64-encoded PNG string. 
  * `result.pdf` contains raw PDF bytes (you can write them to a file).


```
with open("page.pdf", "wb") as f:
  f.write(result.pdf)

```

### 5.4 `ssl_certificate`
If `fetch_ssl_certificate=True`, `result.ssl_certificate` holds details about the site’s SSL cert, such as issuer, validity dates, etc.
## 6. Accessing These Fields
After you run:
```
result = await crawler.arun(url="https://example.com", config=some_config)

```

Check any field:
```
if result.success:
  print(result.status_code, result.response_headers)
  print("Links found:", len(result.links.get("internal", [])))
  if result.markdown_v2:
    print("Markdown snippet:", result.markdown_v2.raw_markdown[:200])
  if result.extracted_content:
    print("Structured JSON:", result.extracted_content)
else:
  print("Error:", result.error_message)

```

**Remember** : Use `result.markdown_v2` for now. It will eventually become `result.markdown`.
## 7. Next Steps
  * **Markdown Generation** : Dive deeper into how to configure `DefaultMarkdownGenerator` and various filters. 
  * **Content Filtering** : Learn how to use `BM25ContentFilter` and `PruningContentFilter`.
  * **Session & Hooks**: If you want to manipulate the page or preserve state across multiple `arun()` calls, see the hooking or session docs. 
  * **LLM Extraction** : For complex or unstructured content requiring AI-driven parsing, check the LLM-based strategies doc.


**Enjoy** exploring all that `CrawlResult` offers—whether you need raw HTML, sanitized output, markdown, or fully structured data, Crawl4AI has you covered!
Site built with [MkDocs](https://docs.crawl4ai.com/core/crawler-result/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/core/crawler-result/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching

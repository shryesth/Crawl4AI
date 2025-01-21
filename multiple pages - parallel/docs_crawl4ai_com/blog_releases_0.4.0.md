[Crawl4AI Documentation](https://docs.crawl4ai.com/blog/releases/0.4.0/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/blog/releases/0.4.0/..>)
  * [ Quick Start ](https://docs.crawl4ai.com/blog/releases/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/blog/releases/0.4.0/<#>)


  * [Home](https://docs.crawl4ai.com/blog/releases/0.4.0/..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/blog/releases/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/blog/releases/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/blog/releases/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/releases/0.4.0/>)
    * [Changelog](https://docs.crawl4ai.com/blog/releases/0.4.0/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/blog/releases/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/blog/releases/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/blog/releases/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/blog/releases/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/blog/releases/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/blog/releases/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/blog/releases/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/blog/releases/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/blog/releases/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/blog/releases/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/blog/releases/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/blog/releases/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/blog/releases/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/blog/releases/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/blog/releases/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/blog/releases/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/blog/releases/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/blog/releases/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/blog/releases/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/blog/releases/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/blog/releases/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/blog/releases/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/blog/releases/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/blog/releases/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/blog/releases/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/blog/releases/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/blog/releases/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/blog/releases/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/blog/releases/api/strategies/>)


  * [Release Summary for Version 0.4.0 (December 1, 2024)](https://docs.crawl4ai.com/blog/releases/0.4.0/<#release-summary-for-version-040-december-1-2024>)
  * [Overview](https://docs.crawl4ai.com/blog/releases/0.4.0/<#overview>)
  * [Major Features and Enhancements](https://docs.crawl4ai.com/blog/releases/0.4.0/<#major-features-and-enhancements>)
  * [Revised Change Logs for Version 0.4.0](https://docs.crawl4ai.com/blog/releases/0.4.0/<#revised-change-logs-for-version-040>)
  * [Experimental Features](https://docs.crawl4ai.com/blog/releases/0.4.0/<#experimental-features>)
  * [Conclusion](https://docs.crawl4ai.com/blog/releases/0.4.0/<#conclusion>)


# Release Summary for Version 0.4.0 (December 1, 2024)
## Overview
The 0.4.0 release introduces significant improvements to content filtering, multi-threaded environment handling, user-agent generation, and test coverage. Key highlights include the introduction of the PruningContentFilter, designed to automatically identify and extract the most valuable parts of an HTML document, as well as enhancements to the BM25ContentFilter to extend its versatility and effectiveness.
## Major Features and Enhancements
### 1. PruningContentFilter
  * Introduced a new unsupervised content filtering strategy that scores and prunes less relevant nodes in an HTML document based on metrics like text and link density.
  * Focuses on retaining the most valuable parts of the content, making it highly effective for extracting relevant information from complex web pages.
  * Fully documented with updated README and expanded user guides.


### 2. User-Agent Generator
  * Added a user-agent generator utility that resolves compatibility issues and supports customizable user-agent strings.
  * By default, the generator randomizes user agents for each request, adding diversity, but users can customize it for tailored scenarios.


### 3. Enhanced Thread Safety
  * Improved handling of multi-threaded environments by adding better thread locks for parallel processing, ensuring consistency and stability when running multiple threads.


### 4. Extended Content Filtering Strategies
  * Users now have access to both the PruningContentFilter for unsupervised extraction and the BM25ContentFilter for supervised filtering based on user queries.
  * Enhanced BM25ContentFilter with improved capabilities to process page titles, meta tags, and descriptions, allowing for more effective classification and clustering of text chunks.


### 5. Documentation Updates
  * Updated examples and tutorials to promote the use of the PruningContentFilter alongside the BM25ContentFilter, providing clear instructions for selecting the appropriate filter for each use case.


### 6. Unit Test Enhancements
  * Added unit tests for PruningContentFilter to ensure accuracy and reliability.
  * Enhanced BM25ContentFilter tests to cover additional edge cases and performance metrics, particularly for malformed HTML inputs.


## Revised Change Logs for Version 0.4.0
### PruningContentFilter (Dec 01, 2024)
  * Introduced the PruningContentFilter to optimize content extraction by pruning less relevant HTML nodes.
  * **Affected Files:**
    * **crawl4ai/content_filter_strategy.py** : Added a scoring-based pruning algorithm.
    * **README.md** : Updated to include PruningContentFilter usage.
    * **docs/md_v2/basic/content_filtering.md** : Expanded user documentation, detailing the use and benefits of PruningContentFilter.


### Unit Tests for PruningContentFilter (Dec 01, 2024)
  * Added comprehensive unit tests for PruningContentFilter to ensure correctness and efficiency.
  * **Affected Files:**
    * **tests/async/test_content_filter_prune.py** : Created tests covering different pruning scenarios to ensure stability and correctness.


### Enhanced BM25ContentFilter Tests (Dec 01, 2024)
  * Expanded tests to cover additional extraction scenarios and performance metrics, improving robustness.
  * **Affected Files:**
    * **tests/async/test_content_filter_bm25.py** : Added tests for edge cases, including malformed HTML inputs.


### Documentation and Example Updates (Dec 01, 2024)
  * Revised examples to illustrate the use of PruningContentFilter alongside existing content filtering methods.
  * **Affected Files:**
    * **docs/examples/quickstart_async.py** : Enhanced example clarity and usability for new users.


## Experimental Features
  * The PruningContentFilter is still under experimental development, and we continue to gather feedback for further refinements.


## Conclusion
This release significantly enhances the content extraction capabilities of Crawl4ai with the introduction of the PruningContentFilter, improved supervised filtering with BM25ContentFilter, and robust multi-threaded handling. Additionally, the user-agent generator provides much-needed versatility, resolving compatibility issues faced by many users.
Users are encouraged to experiment with the new content filtering methods to determine which best suits their needs.
Site built with [MkDocs](https://docs.crawl4ai.com/blog/releases/0.4.0/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/blog/releases/0.4.0/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching

Scrapy_test_project
===================

A simple Scrapy practice which will get the torrent links and names, and then save results to files.

(still under development)

## Basic scrapy instructions:

* scrapy startproject [project_name|ex:get_torrent] : create your new project
* scrapy genspider -t [template_name|ex:crawl] [spider_name|ex:blog_spider] [scraped_domain|ex:blog.com] : create your spider from template
* scrapy crawl [project_name|ex:get_torrent] : start crawling data

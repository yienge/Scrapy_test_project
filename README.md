Scrapy_test_project
===================

A simple Scrapy practice which will get the torrent links and names,
and then save result data to files and local elasticsearch.

(still under development)

## Tutorials:

* scrapy http://blog.jobbole.com/73115/ (chinese)
* scrapy http://doc.scrapy.org/en/latest/intro/tutorial.html (english)
* elasticsearch http://www.elasticsearch.org/

## Scrapy Snippets:

* http://snipplr.com/all/tags/scrapy/
* https://github.com/scrapinghub/testspiders

## Required:

* To use query functionality, you need to install elasticsearch first. Please download it from http://www.elasticsearch.org/
* Once you have installed elasticsearch, run the scrapy project, and then the data will be imported into elasticsearch.

## instructions:

* scrapy startproject get_torrent : create your new project
* scrapy genspider -t crawl dmhy dmhy.org : create your spider from template
* scrapy crawl dmhy : start crawling data
* scrapy crawl dmhy -s LOG_FILE=my_scrapy.log

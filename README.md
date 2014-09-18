Scrapy_test_project
===================

A simple Scrapy practice which will get the torrent links and names, and then save results to files.

(still under development)

## Tutorial:

* http://blog.jobbole.com/73115/ (chinese)
* http://doc.scrapy.org/en/latest/intro/tutorial.html (english)

## instructions:

* scrapy startproject get_torrent : create your new project
* scrapy genspider -t crawl dmhy dmhy.org : create your spider from template
* scrapy crawl dmhy : start crawling data
* scrapy crawl dmhy -s LOG_FILE=my_scrapy.log

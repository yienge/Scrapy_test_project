from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from get_torrent.items import Website, Page


class DmhySpider(CrawlSpider):
    name = 'dmhy'
    allowed_domains = ['dmhy.org']
    start_urls = [
        "http://share.dmhy.org/topics/list/sort_id/2/page/1",
    ]

    rules = (
        # this rule indicates what function will parse topics/list e.g. get next page
        # Rule(SgmlLinkExtractor(allow=('topics\/list', )), callback='parse_list'),

        # this rule indicates what function will parse topics/view
        Rule(SgmlLinkExtractor(allow=('topics\/view', )), callback='parse_view'),
    )

    def parse_list(self, response):
        hxs = Selector(response)
        topics = hxs.xpath('//table[@id="topic_list"]/tbody/tr/td[@class="title"]')
        items = []

        for topic in topics:
            item = Website()
            item['name'] = topic.xpath('a/text()').extract()
            item['url'] = topic.xpath('a/@href').extract()
            # item['description'] = topic.xpath('text()').re('-\s([^\n]*?)\\n')
            items.append(item)

        return items

    def parse_view(self, response):
        hxs = Selector(response)
        topics = hxs.xpath('//div[@id="tabs-1"]/p')
        topic_info = hxs.xpath('//div[@class="resource-info"]/ul/li/span')
        pages = []

        for topic in topics:
            page = Page()
            page['name'] = topic.xpath('a/text()').extract()
            page['url'] = topic.xpath('a/@href').extract()
            page['date'] = topic_info.xpath('text()').extract()
            # page['description'] = topic.xpath('a/text()').re('-\s([^\n]*?)\\n')
            pages.append(page)

        return pages

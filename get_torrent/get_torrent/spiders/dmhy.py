# coding=utf-8
import re
import sys

from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from get_torrent.items import Website, Page

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')


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

        topic_infos = hxs.xpath('//div[contains(@class, "resource-info")]/ul/li/span/text()')
        pattern = re.compile('.*/.*/.* .*:.*')
        for info in topic_infos:
            data = info.extract()
            if pattern.match(data) is not None:
                file_uploaded_date = data
            elif 'MB' or 'GB' in data:
                file_size = data

        topics = hxs.xpath('//div[@id="tabs-1"]/p')

        for topic in topics:
            try:
                tab_name = topic.xpath('a/text()').extract().pop()
                tab_url = topic.xpath('a/@href').extract().pop()
            except AttributeError:
                pass
            except IndexError:
                pass

            if tab_name and "magnet" not in tab_name and "谷歌" not in tab_name:
                name = tab_name
                url = tab_url

        page = Page()
        page['name'] = name
        page['url'] = url
        if file_size:
            page['size'] = file_size
        else:
            page['size'] = ''

        if file_uploaded_date:
            page['date'] = file_uploaded_date
        else:
            page['date'] = ''

        return page

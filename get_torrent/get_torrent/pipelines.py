# coding=utf-8

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')


class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their description"""

    def __init__(self):
        self.file = open('result.txt', 'w')
        self.file_with_complete_data = open('result_total.txt', 'w')
        self.url_prefix = 'http://share.dmhy.org'

    def __del__(self):
        self.file.close()
        self.file_with_complete_data.close()

    def process_item(self, item, spider):
        if len(item['url']) and len(item['name']):
            url = unicode(item['url'].pop())
            link_title = unicode(item['name'].pop()).lower()

            if link_title and "magnet" not in link_title and "谷歌" not in link_title:
                self.save_all_data(url, link_title)
                self.save_specific_data(url, link_title)

        return item

    def save_all_data(self, url, link_title):
        self.file_with_complete_data.write(
            'name: ' + link_title.strip() + '\n' +
            'URL: ' + self.url_prefix + url.strip() + '\n\n'
        )

    def save_specific_data(self, url, link_title):
        # translation_group = ['Dymy']
        title_keywords = ['hunter', 'fairy', 'haikyuu']

        # for group in translation_group:
        for keywords in title_keywords:
            # if group in link_title and keywords in link_title:
            if keywords in link_title:
                self.file.write(
                    'name: ' + link_title.strip() + '\n' +
                    'URL: ' + self.url_prefix + url.strip() + '\n\n'
                )


class FileWriterPipeline(object):

    def process_item(self, item, spider):
        return item


class DBWriterPipeline(object):

    def process_item(self, item, spider):
        return item

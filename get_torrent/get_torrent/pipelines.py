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
        self.file2 = open('result_total.txt', 'w')

    def process_item(self, item, spider):
        # translation_group = ['Dymy']
        title_keywords = ['hunter', 'fairy', 'haikyuu']

        url_prefix = 'http://share.dmhy.org'

        if len(item['url']) and len(item['name']):
            url = unicode(item['url'].pop())
            link_title = unicode(item['name'].pop()).lower()

            if link_title and "magnet" not in link_title and "谷歌" not in link_title:

                # for group in translation_group:
                for keywords in title_keywords:
                    # if group in link_title and keywords in link_title:
                    if keywords in link_title:
                        self.file.write(
                            'name: ' + link_title.strip() + '\n' +
                            'URL: ' + url_prefix + url.strip() + '\n\n'
                        )

                self.file2.write(
                    'name: ' + link_title.strip() + '\n' +
                    'URL: ' + url_prefix + url.strip() + '\n\n'
                )

        return item


class FileWriterPipeline(object):

    def process_item(self, item, spider):
        return item


class DBWriterPipeline(object):

    def process_item(self, item, spider):
        return item

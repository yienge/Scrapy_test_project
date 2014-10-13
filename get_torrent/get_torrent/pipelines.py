# coding=utf-8

# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import requests
import json

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')


class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their description"""

    def __init__(self):
        self.file_with_complete_data = open('result_total.txt', 'w')
        self.url_prefix = 'http://share.dmhy.org'

    def __del__(self):
        self.file_with_complete_data.close()

    def process_item(self, item, spider):
        if len(item['url']) and len(item['name']):
            url        = unicode(item['url'])
            link_title = unicode(item['name']).lower()
            date       = unicode(item['date'])
            file_size  = unicode(item['size'])
            serial     = item['serial']
            self.save_all_data(url, link_title, date, file_size)
            self.save_data_to_es(serial, url, link_title, date, file_size)

        return item

    def save_all_data(self, url, link_title, date, file_size):
        self.file_with_complete_data.write(
            'name: ' + link_title.strip() + '\n' +
            'URL: ' + self.url_prefix + url.strip() + '\n' +
            'date: ' + date.strip() + '\n' +
            'size: ' + file_size.strip() + 'MB\n\n'
        )

    def save_data_to_es(self, serial, url, link_title, date, file_size):
        payload = json.dumps({
            'link'        : link_title,
            'url'         : self.url_prefix + url.strip(),
            'insert_date' : date.strip(),
            'size'        : file_size.strip(),
        })

        post_url = 'http://127.0.0.1:9200/torrent/dmhy/%s' % serial
        requests.post(post_url, data=payload)
        pass


class FileWriterPipeline(object):

    def process_item(self, item, spider):
        return item

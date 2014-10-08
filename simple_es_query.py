#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
# import pprint


def process_result(r):
    raw_res = r.json()
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(raw_res['hits']['hits'])

    for item in raw_res['hits']['hits']:
        result = item['_source']
        print result['link']
        print result['url']
        print

keyword = raw_input('query:')
count = raw_input('result number:')
if keyword:
    r = requests.get('http://127.0.0.1:9200/dmhy/torrent/_search?q=' + keyword)
    process_result(r)
else:
    if not count:
        count = '50'

    r = requests.get('http://127.0.0.1:9200/dmhy/torrent/_search?pretty=true&q=*:*&size=' + count)
    process_result(r)

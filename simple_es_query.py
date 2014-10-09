#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
# import pprint
import json


def process_result(r):
    raw_res = r.json()
    # pp = pprint.PrettyPrinter(indent=2)
    # pp.pprint(raw_res)

    if raw_res['hits']:
        for item in raw_res['hits']['hits']:
            result = item['_source']
            print result['link']
            print result['url']
            print result['insert_date']
            print

keyword = raw_input('query:')
count = raw_input('result number:')

if not count:
    count = '50'

if keyword:
    payload = json.dumps({
        'query': {'term': {'link': keyword}},
        'sort': [{'insert_date': {'order': 'asc'}}],
        'size': count
    })
    r = requests.post('http://127.0.0.1:9200/torrent/dmhy/_search',
                      data=payload)
else:
    r = requests.get('http://127.0.0.1:9200/torrent/dmhy/_search?pretty=true&q=*:*&size=' + count)

process_result(r)

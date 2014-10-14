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
        print '共' + str(raw_res['hits']['total']) + '筆'
        for item in raw_res['hits']['hits']:
            result = item['_source']
            print 'name: %s\nurl : %s\ndate: %s\nsize: %s' % (result['link'], result['url'], result['insert_date'], result['size'])
            print


keyword = raw_input('query:')
serial = raw_input('serial:')
insert_date_order = raw_input('insert_date order:')
count = raw_input('result number:')

if not insert_date_order:
    insert_date_order = 'desc'

if not count:
    count = '50'

if serial:
    r = requests.get('http://127.0.0.1:9200/torrent/dmhy/%s' % serial)
    res = r.json()
    data = res['_source']
    print data['link']
    print data['url']
    print data['insert_date']
    print data['size']
elif keyword:
    payload = json.dumps({
        'query': {'term': {'link': keyword}},
        'sort': [
            {'insert_date': {'order': insert_date_order, 'mode': 'avg'}},
            {'size': 'desc'},
            "_score"
        ],
        'size': count
    })
    r = requests.post('http://127.0.0.1:9200/torrent/dmhy/_search',
                      data=payload)
    process_result(r)
else:
    r = requests.get('http://127.0.0.1:9200/torrent/dmhy/_search?pretty=true&q=*:*&size=' + count)
    process_result(r)

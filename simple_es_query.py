#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import pprint

keyword = raw_input('query:')
r = requests.get('http://127.0.0.1:9200/dmhy/torrent/_search?q=' + keyword)
raw_res = r.json()

pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(raw_res['hits']['hits'])

for item in raw_res['hits']['hits']:
    result = item['_source']
    print result['url']
    print result['link']

#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import pprint

payload = '<p>this is a test</p>'

# r = requests.get('http://127.0.0.1:9200/_status')
r = requests.get('http://127.0.0.1:9200/torrent/_status')
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(r.json())

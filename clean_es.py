#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import pprint

r = requests.delete('http://127.0.0.1:9200/torrent/')
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(r)

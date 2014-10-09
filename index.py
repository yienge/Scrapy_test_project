#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import pprint

payload = '<p>this is a test</p>'

# test standard analyzer
# r = requests.get('http://127.0.0.1:9200/_analyze?analyzer=standard', data=payload)

# test lowercase filter
# r = requests.get('http://127.0.0.1:9200/_analyze?tokenizer=keyword&filters=lowercase', data=payload)

# test html_strip char filter
# r = requests.get('http://127.0.0.1:9200/_analyze?tokenizer=keyword&token_filters=lowercase&char_filters=html_strip', data=payload)

# test the tokenizer of the torrent index
# r = requests.get('http://127.0.0.1:9200/torrent/_analyze?text=this+is+a+test')

# get index settings
r = requests.get('http://127.0.0.1:9200/torrent/_settings')

# get all indices settings
# r = requests.get('http://127.0.0.1:9200/_all/_settings')

# if you wanna change index analysis, you have to close, then change, and reopen index
settings = {
    'analysis': {
        'analyzer': {
            'content': {
                'type': 'custom',
                'tokenizer': 'whitespace'
            }
        }
    }
}

# close index
r = requests.get('http://127.0.0.1:9200/_all/_close')

# change index analyzer
r = requests.put('http://127.0.0.1:9200/torrent/_settings', data=settings)
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(r.json())

# open index
r = requests.get('http://127.0.0.1:9200/_all/_open')

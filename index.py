#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import pprint

# elasticsearch config example
# https://gist.github.com/clintongormley/1088986

payload = '七原罪'

cmd = raw_input("cmd:")

if not cmd:
    print 'plz enter cmd'
    return

if cmd == 'analyze':
    # test standard analyzer
    r = requests.get('http://127.0.0.1:9200/_analyze?analyzer=standard', data=payload)

    # test lowercase filter
    # r = requests.get('http://127.0.0.1:9200/_analyze?tokenizer=keyword&filters=lowercase', data=payload)

    # test html_strip char filter
    # r = requests.get('http://127.0.0.1:9200/_analyze?tokenizer=keyword&token_filters=lowercase&char_filters=html_strip', data=payload)

    # test the tokenizer of the torrent index
    # r = requests.get('http://127.0.0.1:9200/torrent/_analyze?text=this+is+a+test')
elif cmd == 'setting':
    # get index settings
    r = requests.get('http://127.0.0.1:9200/torrent/_settings')

    # get all indices settings
    # r = requests.get('http://127.0.0.1:9200/_all/_settings')
elif cmd == 'query':
    # request
    r = requests.get('http://127.0.0.1:9200/torrent', data=payload)
elif cmd == 'set_index':
    # if you wanna change index analysis, you have to close, then change, and reopen index
    settings_for_using_ngram = {
        "mappings": {
            "dmhy": {
                "properties": {
                    "url": {
                        "type": "string",
                        "analyzer": "url_ngram"
                    },
                    "link": {
                        "type": "string"
                    },
                }
            }
        },
        "settings": {
            "analysis": {
                "filter": {
                    "url_ngram": {
                        "side": "front",
                        "min_gram": 1,
                        "max_gram": 10,
                        "type": "edgeNGram"
                    },
                },
                # "tokenizer": {
                    # "custom_tokenizer": {
                        # "type": "standard",
                        # "max_token_length": 900,
                        # "buffer_size": 512
                    # }
                # },
                "analyzer": {
                    "link_name": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": [
                            "standard",
                            "lowercase",
                            "url_ngram",
                            "asciifolding"
                        ]
                    },
                }
            }
        }
    }

    # close index
    r = requests.get('http://127.0.0.1:9200/_all/_close')

    # change index analyzer
    r = requests.put('http://127.0.0.1:9200/torrent/_settings', data=settings_for_using_ngram)

    # open index
    r = requests.get('http://127.0.0.1:9200/_all/_open')

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(r.json())

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

with open("jawiki-country.json") as f:
    articles = f.read().split('\n')
    for article in articles:
        article_dict = json.loads(article)
        if article_dict["title"] == u"イギリス":
            print(article_dict["text"])
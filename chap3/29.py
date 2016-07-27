#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import json
import requests

start = re.compile(r"^\{\{基礎情報")
end = re.compile(r"\}\}$")
pattern = re.compile(r"^\|\s?(.*?)\s=\s(.*)")

wikipedia_api = "http://ja.wikipedia.org/w/api.php?"
params = {
    'action': "query",
    'prop': "imageinfo",
    'iiprop': "url",
    'format': "json",
    'formatversion': '2',
    'utf8': '',
    'continue': ''
}

with open("england.txt") as f:
    dic = {}
    flg = False
    for line in f.readlines():
        if start.match(line):
            flg = True
            continue
        elif end.match(line):
            flg = False

        if flg:
            l = pattern.match(line)
            if l:
                dic[l.group(1)] = l.group(2)

    filename = dic.get("国旗画像")
    params['titles'] = "Image: %s" % filename
    res = requests.get(url=wikipedia_api, params=params)
    datum = json.loads(res.text)
    try:
        file_url = datum['query']['pages'][0]['imageinfo'][0]['url']
        print file_url
    except:
        print(datum)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

start = re.compile(r"^\{\{基礎情報")
end = re.compile(r"\}\}$")
pattern = re.compile(r"^\|\s?(.*?)\s=\s(.*)")

def remove_link(string):
    link = re.compile(r"\[\[((.+?)\|)?(.+?)\]\]")
    return link.sub(r"\3", string)

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
                dic[l.group(1)] = remove_link(l.group(2))

    print str(dic).decode('string-escape')
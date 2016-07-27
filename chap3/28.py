#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

start = re.compile(r"^\{\{基礎情報")
end = re.compile(r"\}\}$")
pattern = re.compile(r"^\|\s?(.*?)\s=\s(.*)")

def remove_markups(string):
    markups = (
        re.compile(r"\[https?://[a-zA-Z0-9\./]+\s(.+)?\]"),
        re.compile(r"#REDIRECT\s?(.+)"),
        re.compile(r"<!--\s?(.+)\s?-->"),
        re.compile(r"\{\{.*[Ll]ang\|[a-zA-Z\-]+\|(.+)\}\}"),
        re.compile(r"(.*)<ref.+(</ref>)?>"),
        re.compile(r"(.*?)<br\s?/?>"),
        re.compile(r"<[a-z]+.*>(.*?)</[a-z]+>"),
        re.compile(r"\[\[((.+?)\|)?(.+?)\]\]")
    )
    for markup in markups:
        if markup.match(string):
            string = markup.sub(r"\1", string)
    return string

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
                dic[l.group(1)] = remove_markups(l.group(2))

    print str(dic).decode('string-escape')
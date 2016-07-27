#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

start = re.compile(r"^\{\{基礎情報")
end = re.compile(r"\}\}$")
pattern = re.compile(r"^\|\s?(.*?)\s=\s(.*)")

def remove_emphasis(string):
    emphasis = re.compile(r"''('*)(.+)''\1")
    return emphasis.sub(r"\2", string)

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
                dic[l.group(1)] = remove_emphasis(l.group(2))

    print str(dic).decode('string-escape')
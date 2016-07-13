#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

pattern = r"Category"
compiled = re.compile(pattern)

with open("england.txt") as f:
    for line in f.readlines():
        if compiled.findall(line):
            print line
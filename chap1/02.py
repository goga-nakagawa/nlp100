#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import izip

def alternateStr(s1, s2):
    return "".join([c1 + c2 for c1, c2 in izip(s1, s2)])

print alternateStr(u"パトカー", u"タクシー")
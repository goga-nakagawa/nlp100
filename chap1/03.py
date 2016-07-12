#!/usr/bin/env python
# -*- coding: utf-8 -*-

def countChar(s):
    return [len(word) for word in s.replace(".", "").replace(",", "").split(" ")]

print countChar("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.")
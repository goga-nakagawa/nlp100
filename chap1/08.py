#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cipher(s):
    return "".join([chr(219 - ord(c)) if ord(c) in xrange(97, 123) else c for c in s])

print cipher("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
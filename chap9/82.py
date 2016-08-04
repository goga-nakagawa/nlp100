#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint

with open("combined.txt", "rb") as infile:
    with open("context.txt", "wb") as outfile:
        for l in infile.readlines():
            words = l.split()
            for word in words:
                sample_num = randint(1, 5)
                for i in xrange(-sample_num, sample_num+1):
                    if i != 0:
                        ls = [word]
                        try:
                            ls.append(words[-i])
                            outfile.write("\t".join(ls))
                        except IndexError:
                            continue

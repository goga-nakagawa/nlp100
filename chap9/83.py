#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
f(t,c): 単語tと文脈語cの共起回数
f(t,∗): 単語tの出現回数
f(∗,c): 文脈語cの出現回数
N: 単語と文脈語のペアの総出現回数
"""

from collections import Counter

class Corpus:
    def __init__(self):
        self.f_tc = Counter()
        self.f_t = Counter()
        self.f_c = Counter()
        self.N = Counter()

    def put_context(self):
        with open("context.txt", "rb") as infile:
            for l in infile.readlines():
                t, c = l.split("\t")[0], l.split("\t")[1]
                self.f_tc[(t, c)] += 1
                self.f_t[t] += 1
                self.f_c[c] += 1
                # self.N[set([t, c])] += 1


cp = Corpus()
cp.put_context()
print cp.f_t.most_common(100)

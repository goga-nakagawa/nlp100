#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

class Sentiment:
    def __init__(self):
        self.pos_neg = []

    def put_data(self, polarity=None):
        if polarity == "pos":
            with open("rt-polarity.pos") as f:
                for l in f.readlines():
                    self.pos_neg += [["+1",l]]
        elif polarity == "neg":
            with open("rt-polarity.neg") as f:
                for l in f.readlines():
                    self.pos_neg += [["-1",l]]

    def shuffle(self):
        random.shuffle(self.pos_neg) #in-place shuffle
        return self.pos_neg


s = Sentiment()
s.put_data(polarity="pos")
s.put_data(polarity="neg")

pos_cnt = 0
neg_cnt = 0
with open("sentiment.txt", "wb") as f:
    for l in s.shuffle():
        f.write(" ".join(l))
        if l[0] == "+1":
            pos_cnt += 1
        elif l[0] == "-1":
            neg_cnt += 1

print pos_cnt, neg_cnt




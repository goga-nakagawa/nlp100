#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import numpy as np
import random
from collections import defaultdict
from stop_words import get_stop_words
from nltk.stem import PorterStemmer


class LogisticRegression:
    def __init__(self, eta0=0.6, etan=0.9999):
        self.weights = defaultdict(float)
        self.eta0 = eta0
        self.etan = etan

    def is_stop_words(self, word):
        return word.strip().lower() in get_stop_words("en")

    def predict(self, features):
        x = sum([self.weights[feature] for feature in features])
        return 1.0 / (1.0 + np.exp(-x))

    def update(self, features, polarity, eta):
        predict_answer = self.predict(features)
        actual_answer = (polarity + 1) / 2

        for feature in features:
            dif = eta * (predict_answer - actual_answer)
            self.weights[feature] -= dif

    def calc_weights(self):
        stemmer = PorterStemmer()
        with open("sentiment.txt") as f:
            p = re.compile(r"^(\+1\s|\-1\s)(.*?)\n$")
            s = re.compile(r"[,.:;\s]")
            for index, l in enumerate(f.readlines()):
                sentence = p.match(l)
                features = []
                if sentence:
                    polarity = float(sentence.group(1).strip())
                    words = s.split(sentence.group(2).strip())
                    for w in words:
                        if not self.is_stop_words(w) and w:
                            try:
                                features.append(stemmer.stem(w))
                            except UnicodeDecodeError:
                                continue
                    self.update(features, polarity, self.eta0 * (self.etan ** index))

    def calc_correct_rate(self):
        
lr = LogisticRegression()
lr.calc_weights()
weights = sorted(lr.weights.items(), key=lambda x: x[1])
print weights[:10]
print weights[-10:]


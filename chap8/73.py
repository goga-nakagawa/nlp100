#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import numpy as np
import random
from collections import defaultdict
from stop_words import get_stop_words
from nltk.stem import PorterStemmer


def is_stop_words(word):
    return word.strip().lower() in get_stop_words("en")


class Feature:
    def __init__(self):
        self.features = []

    def put_data(self):
        features = set()
        with open("sentiment.txt") as f:
            pol = re.compile(r"^(\+1\s|\-1\s)(.*?)\n$")
            word = re.compile(r"[,.:;\s]")
            stemmer = PorterStemmer()
            for l in f.readlines():
                sent = pol.match(l)
                if sent:
                    polarity = sent.group(1).strip()
                    sentence = sent.group(2).strip()
                    words = word.split(sentence)
                    for w in words:
                        if not is_stop_words(w) and w:
                            try:
                                features.add(stemmer.stem(w))
                            except UnicodeDecodeError:
                                # case when w has not alphabetic character
                                continue
        self.features = list(features)


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



class LogisticRegression:
    def __init__(self):
        self.weights = defaultdict(float)

    def predict(self, features):
        x = sum([self.weights[feature] for feature in features])
        return 1.0 / (1.0 + np.exp(-x))

    def update(self, features, polarity, eta):
        predict_answer = self.predict(features)
        actual_answer = (float(polarity) + 1) / 2

        for feature in features:
            dif = eta * (predict_answer - actual_answer)
            if 0.0002 > abs(self.weights[feature] - dif):
                continue
            self.weights[feature] -= dif

    def calc_weights(self, sentiments, eta0=0.6, etan=0.9999):
        for idx, sentiment in enumerate(sentiments):
            self.update(sentiment[1], sentiment[0], eta0 * (etan ** idx))

    def save_weights(self, file_name):
        with open(file_name, 'wb') as f:
            for k, v in sorted(self.weights.items(), key=lambda x: x[1]):
                f.write('{}\t{}\n'.format(k, v))

    def restore_weights(self, file_name):
        weights = {}
        with open(file_name) as f:
            for l in f.readlines():
                key, value = l.split()
                weights[key] = float(value)
        self.weights = weights


s = Sentiment()
s.put_data(polarity="pos")
s.put_data(polarity="neg")

# f = Feature()
# f.put_data()

lr = LogisticRegression()
lr.calc_weights(sentiments=s.shuffle())

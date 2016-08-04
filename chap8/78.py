#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import numpy as np
import random
from collections import defaultdict
from stop_words import get_stop_words
from nltk.stem import PorterStemmer


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
        with open("sentiment_training.txt") as f:
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

    def calc_score(self):
        stemmer = PorterStemmer()
        cnt = 0
        correct_count = 0
        actual_positive_count = 0
        predict_positive_count = 0
        correct_positive_count = 0
        with open("sentiment_examine.txt") as f:
            p = re.compile(r"^(\+1\s|\-1\s)(.*?)\n$")
            s = re.compile(r"[,.:;\s]")
            for index, l in enumerate(f.readlines()):
                sentence = p.match(l)
                features = []
                if sentence:
                    cnt += 1
                    polarity = float(sentence.group(1).strip())
                    words = s.split(sentence.group(2).strip())
                    for w in words:
                        if not self.is_stop_words(w) and w:
                            try:
                                features.append(stemmer.stem(w))
                            except UnicodeDecodeError:
                                continue
                    calc_polarity = 1.0 if sum([self.weights[f] for f in features]) > 0 else -1.0
                    if calc_polarity == polarity:
                        correct_count += 1
                    if polarity == 1.0:
                        actual_positive_count += 1
                    if calc_polarity == 1.0:
                        predict_positive_count += 1
                    if calc_polarity == polarity and calc_polarity == 1.0:
                        correct_positive_count += 1

        precision_rate = 1.0*correct_positive_count / predict_positive_count
        recall_rate = 1.0*correct_positive_count / actual_positive_count
        f_value = (2 * precision_rate * recall_rate) / (precision_rate + recall_rate)
        return precision_rate, recall_rate, f_value


s = Sentiment()
s.put_data(polarity="pos")
s.put_data(polarity="neg")

with open("sentiment_training.txt", "wb") as t:
    with open("sentiment_examine.txt", "wb") as e:
        for index, l in enumerate(s.shuffle()):
            if index % 5 == 0:
                e.write(" ".join(l))
            else:
                t.write(" ".join(l))


lr = LogisticRegression()
lr.calc_weights()
print lr.calc_score()

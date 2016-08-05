#!/usr/bin/env python
# -*- coding: utf-8 -*-

import word2vec

class Word2Vec:
    def __init__(self, model=None):
        self.word2vec = word2vec
        self.model = model

    def training(self, infile, outfile):
        self.word2vec.word2vec(
                infile,
                outfile,
                size=100,
                verbose=True
                )
        self.model = self.word2vec.load(outfile)

    def training_clusters(self, infile, outfile):
        self.word2vec.word2clusters(
                infile,
                outfile,
                100,
                verbose=True
                )

    def predict_word(self, w):
        return self.model[w]

    def predict_similarity(self, w1, w2):
        indexes, metrics = self.model.cosine(w1)
        ls = self.model.generate_response(indexes, metrics).tolist()
        return tuple(filter(lambda x: x[0] == w2, ls)[0])[1]

    def predict_most_similar(self, w, n):
        indexes, metrics = self.model.cosine(w)
        ls = self.model.generate_response(indexes, metrics).tolist()
        return sorted(ls, key=lambda x: x[1], reverse=True)[:n]

    def predict_analogies(self, n, **kwargs):
        try:
            indexes, metrics = self.model.analogy(pos=kwargs.get("pos"), neg=kwargs.get("neg"), n=n)
            return self.model.generate_response(indexes, metrics).tolist()
        except KeyError:
            return [(u"key not found", 0)]

w2v = Word2Vec()
w2v.training("combined.txt", "trainied.bin")

with open("family.txt", "rb") as infile:
    with open("family_validated.txt", "wb") as outfile:
        for l in infile.readlines():
            w1, w2, w3 = l.split()[0], l.split()[1], l.split()[2]
            l += " ".join([str(x) for x in w2v.predict_analogies(1, pos=[w2, w3], neg=[w1])[0]])
            outfile.write(l)

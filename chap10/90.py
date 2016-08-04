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
        indexes, metrics = self.model.analogy(pos=kwargs.get("pos"), neg=kwargs.get("neg"), n=n)
        return self.model.generate_response(indexes, metrics).tolist()

w2v = Word2Vec()
w2v.training("combined.txt", "trainied.bin")

print "86: %s" % w2v.predict_word("United_States")
# print "87: %s" % w2v.predict_similarity("United_States", "U.S")
print "88: \n%s" % "\n".join([x[0] + ": " + str(x[1]) for x in w2v.predict_most_similar("England", 10)])
print "89: \n%s" % "\n".join([x[0] + ": " + str(x[1]) for x in w2v.predict_analogies(10, pos=["Spain", "Athens"], neg=["Madrid"])])

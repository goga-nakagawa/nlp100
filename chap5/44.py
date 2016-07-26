#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import pydot
eos = re.compile(r"^EOS")
astrisk = re.compile(r"^\*(.*?)")
parse = re.compile(r"\t|\,")

class Morph:
    def __init__(self, surface=None, base=None, pos=None, pos1=None):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return "surface: %s, base: %s, pos: %s, pos1: %s" % (self.surface, self.base, self.pos, self.pos1)


class Chunk:
    def __init__(self, dst=None, srcs=None):
        self.morphs = []
        self.dst = dst
        self.srcs = srcs

    def __str__(self):
        return "dst: %s, srcs: %s" % (self.dst, self.srcs)

    def add_morph(self, Morph):
        self.morphs.append(Morph)

    def get_morphs(self):
        return ''.join([m.surface for m in self.morphs if m.pos != "記号"])

    def has_verb(self):
        return "動詞" in [m.pos for m in self.morphs]

    def has_noun(self):
        return "名詞" in [m.pos for m in self.morphs]


sentences = []
sentence = []
chunk = None

with open('neko.txt.cabocha') as f:

    for line in f.readlines():
        eosed = eos.match(line)
        astrisked = astrisk.match(line)
        parsed = parse.split(line)

        if eosed:
            sentences.append(sentence)
            sentence = []
        elif astrisked:
            kakari = line.split()
            chunk = Chunk(
                        dst=int(kakari[2].strip("D")),
                        srcs=int(kakari[1])
                )
            sentence.append(chunk)
        elif parsed and len(parsed) == 10:
            morph = Morph(
                        surface=parsed[0],
                        base=parsed[7],
                        pos=parsed[1],
                        pos1=parsed[2]
                    )
            chunk.add_morph(morph)



for index, sentence in enumerate(sentences[101:105]):
    for chunk in sentence:
        edges = []
        if chunk.dst > -1 and chunk.get_morphs():
            edges.append((chunk.get_morphs(), sentence[chunk.dst].get_morphs()))
        g = pydot.graph_from_edges(edges, directed=True)
        g.write_png("%s.png" % index, prog='dot')

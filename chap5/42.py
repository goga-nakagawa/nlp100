#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
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


for sentence in sentences:
    for chunk in sentence:
        if chunk.dst > -1 and chunk.get_morphs():
            print "\t".join([chunk.get_morphs(), sentence[chunk.dst].get_morphs()])

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


class Sentence:
    def __init__(self):
        self.morphes = []

    def add_morph(self, Morph):
        self.morphes.append(Morph)


sentences = []
with open('neko.txt.cabocha') as f:
    sentence = Sentence()
    for line in f.readlines():
        eosed = eos.match(line)
        astrisked = astrisk.match(line)
        parsed = parse.split(line)

        if astrisked:
            continue
        elif eosed:
            sentences.append(sentence)
            sentence = Sentence()
        elif parsed and len(parsed) == 10:
            morph = Morph(
                        surface=parsed[0],
                        base=parsed[7],
                        pos=parsed[1],
                        pos1=parsed[2]
                    )
            sentence.add_morph(morph)

for morph in sentences[3].morphes:
    print morph
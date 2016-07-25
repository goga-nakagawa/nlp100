#!/usr/bin/env python
# -*- coding: utf-8 -*-

def tabbed_str_to_dict(tabbed_str):
    elements = tabbed_str.split()
    if 0 < len(elements) < 4:
        return {"surface": elements[0], "base": "", "pos": "", "pos1": ""}
    else:
        return {"surface": elements[0], "base": elements[1], "pos": elements[2], "pos1": elements[3]}

def morphemes_to_sentence(morphemes):
    sentences = []
    sentence = []

    for morpheme in morphemes:
        sentence.append(morpheme)
        if morpheme["pos1"] == "記号-句点":
            sentences.append(sentence)
            sentence = []

    return sentences


with open('neko.txt.mecab') as file_wrapper:
    morphemes = [tabbed_str_to_dict(line) for line in file_wrapper]

sentences = morphemes_to_sentence(morphemes)

print morphemes[::100]
print sentences[::100]

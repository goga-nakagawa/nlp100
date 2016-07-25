#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MeCab
import ngram
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def make_analyzed_file(input_file_name, output_file_name):
    _m = MeCab.Tagger("-Ochasen")
    with open(input_file_name, "rb") as input_file:
        with open(output_file_name, "wb") as output_file:
            output_file.write(_m.parse(input_file.read()))

make_analyzed_file('neko.txt', 'neko.txt.mecab')
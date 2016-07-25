#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

pattern = r"\t|\,"
compiled = re.compile(pattern)

fig = plt.figure(figsize=(20, 6))

with open('neko.txt.mecab') as f:
    freq = {}
    for line in f.readlines():
        matched = compiled.split(line)
        if matched and len(matched) == 10:
            if matched[0] in freq:
                freq[matched[0]] += 1
            else:
                freq[matched[0]] = 1
    wordcnt = [(k, v) for k, v in sorted(freq.items(), key=lambda x: x[1], reverse=True)]
    freq = [w[1] for w in wordcnt]
    rank = list(range(1, len(freq) + 1))

    ax3 = fig.add_subplot(133)
    ax3.plot(freq, rank)
    ax3.set_xlabel('Rank')
    ax3.set_ylabel('Frequency')
    ax3.set_title('Zipf low')
    ax3.set_xscale('log')
    ax3.set_yscale('log')
    plt.show()
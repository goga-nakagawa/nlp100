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
    hist = [(k, v) for k, v in sorted(freq.items(), key=lambda x: x[1], reverse=True)]

    x_pos = np.arange(len(hist))
    fp = FontProperties(fname=r'/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc', size=12)

    ax1 = fig.add_subplot(131)
    ax1.bar(x_pos, [f[1] for f in hist], align='center', alpha=0.4)
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels([f[0].decode('utf-8') for f in hist], fontproperties=fp)
    ax1.set_ylabel('Frequency')
    ax1.set_title('Histgram')
    plt.show()
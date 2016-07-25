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
    top10 = [(k, v) for k, v in sorted(freq.items(), key=lambda x: x[1], reverse=True)][:10]

    x_pos = np.arange(len(top10))
    fp = FontProperties(fname=r'/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc', size=12)

    ax1 = fig.add_subplot(131)
    ax1.bar(x_pos, [f[1] for f in top10], align='center', alpha=0.4)
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels([f[0].decode('utf-8') for f in top10], fontproperties=fp)
    ax1.set_ylabel('Frequency')
    ax1.set_title('Top 10 frequent words')
    plt.show()
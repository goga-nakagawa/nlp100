#!/usr/bin/env python
# -*- coding: utf-8 -*-
import CaboCha

def make_analyzed_file(input_file_name, output_file_name):
    _c = CaboCha.Parser()
    with open(input_file_name, "rb") as input_file:
        with open(output_file_name, "wb") as output_file:
            for line in input_file:
                tree = _c.parse(line.lstrip())
                output_file.write(tree.toString(CaboCha.FORMAT_LATTICE))

make_analyzed_file('neko.txt', 'neko.txt.cabocha')
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def concat(x, y, z):
    return unicode(x) + u"時の" + unicode(y) + u"は" + unicode(z)

print concat(12, u"気温", 22.4)
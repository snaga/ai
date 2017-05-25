#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import operator
import unicodedata
from collections import OrderedDict

def getwidechar(s):
    s2 = ""
    for c in s:
        if not unicodedata.name(c).startswith('LATIN'):
            s2 = s2 + c
    return s2

def outputtarget(s):
    for c in getwidechar(s):
        print(c)

def uniqc(a):
    assert isinstance(a, list)
    d = {}
    for e in a:
        d[e] = d.get(e, 0) + 1
    return d

def sortn(d):
    assert isinstance(d, dict)
    l = []
    for i in sorted(d.items(),
                    key=operator.itemgetter(1),
                    reverse=True):
        l.append(i)
    return l

def make3gram(s):
    return make_ngram(s, n=3)

def make2gram(s):
    return make_ngram(s, n=2)

def make_ngram(s, n=3):
    s = getwidechar(s)
    g = []
    for i in range(0, len(s) - (n-1)):
        g.append(s[i:i+n])
    return g

if __name__ == '__main__':
    s = u"親譲りの無鉄砲で小供の時から損ばかりしている。小学校に居る時分学校の二階から飛び降りて一週間ほど腰を抜かした事がある。なぜそんな無闇をしたと聞く人があるかも知れぬ。別段深い理由でもない。新築の二階から首を出していたら、同級生の一人が冗談に、いくら威張っても、そこから飛び降りる事は出来まい。弱虫やーい。と囃したからである。小使に負ぶさって帰って来た時、おやじが大きな眼をして二階ぐらいから飛び降りて腰を抜かす奴があるかと云ったから、この次は抜かさずに飛んで見せますと答えた。"
    print(s)

    t = getwidechar(s)
    print(t)
    outputtarget(t)

    d = uniqc(list(t))
    print(d)
    d = sortn(d)
    print(d)

    for i in d:
        print "%s %s" % (i[0], i[1])

    for t in make3gram(s):
        print(t)

    for t in make2gram(s):
        print(t)

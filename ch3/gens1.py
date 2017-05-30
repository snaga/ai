#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import random
import sys

import MeCab

from ch2 import setrnd

m =  MeCab.Tagger("-Ochasen")
s = u"親譲りの無鉄砲で小供の時から損ばかりしている。小学校に居る時分学校の二階から飛び降りて一週間ほど腰を抜かした事がある。なぜそんな無闇をしたと聞く人があるかも知れぬ。別段深い理由でもない。新築の二階から首を出していたら、同級生の一人が冗談に、いくら威張っても、そこから飛び降りる事は出来まい。弱虫やーい。と囃したからである。小使に負ぶさって帰って来た時、おやじが大きな眼をして二階ぐらいから飛び降りて腰を抜かす奴があるかと云ったから、この次は抜かさずに飛んで見せますと答えた。"
#s = u"この本を手にされたうちの多くの方は、人工知能という言葉を耳にしたことがあると思います。またおそらく、人工無能という表現を見かけたこともあるのではないでしょうか。"

def cutnav(s, nav):
    s_enc = s.encode('utf-8')
    assert isinstance(s_enc, str)
    node = m.parseToNode(s_enc)
    aa = []
    while node:
#        print(node.feature.decode('utf-8'))
        if node.feature.decode('utf-8').split(',')[0] in (u'BOS/EOS'):
            node = node.next
            continue
        if nav == 'n' and node.feature.decode('utf-8').split(',')[0] == u'名詞':
            aa.append(u'%s' % node.feature.decode('utf-8').split(',')[6])
        if nav == 'v' and node.feature.decode('utf-8').split(',')[0] == u'動詞':
            aa.append(u'%s' % node.feature.decode('utf-8').split(',')[6])
        if nav == 'a' and node.feature.decode('utf-8').split(',')[0] == u'形容詞':
            aa.append(u'%s' % node.feature.decode('utf-8').split(',')[6])
        if nav == 'd' and node.feature.decode('utf-8').split(',')[0] == u'形容動詞':
            aa.append(u'%s' % node.feature.decode('utf-8').split(',')[6])
        node = node.next
    for a in aa:
        assert isinstance(a, unicode)
    return aa

def test_cutnav():
    print('n')
    for a in cutnav(s, 'n'):
        print(a)

    print('v')
    for a in cutnav(s, 'v'):
        print(a)

    print('a')
    for a in cutnav(s, 'a'):
        print(a)

    print('d')
    for a in cutnav(s, 'd'):
        print(a)

def np(nlist):
    return u'%sは' % nlist[setrnd(len(nlist))]

def vp(nlist):
    return u'%s' % vlist[setrnd(len(vlist))]

def sentence(nlist, vlist):
    return np(nlist) + vp(vlist)

if __name__ == '__main__':
    random.seed(1)

    nlist = cutnav(s, 'n')
    vlist = cutnav(s, 'v')

    for i in range(0,20):
        print sentence(nlist, vlist)

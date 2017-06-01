#!/usr/bin/env python2.7

import re
import sys

ignore_tags = [
    'programlisting',
    'screen',
    'informaltable',
    'indexterm',
    'variablelist']

def has_ignore_tag_open(l):
    for tag in ignore_tags:
        if l.find('<' + tag + '>') >= 0:
            return True
        if l.find('<' + tag + ' ') >= 0:
            return True
    return False

def has_ignore_tag_close(l):
    for tag in ignore_tags:
        if l.find('</' + tag + '>') >= 0:
            return True
    return False

def get_paragraph(f):
    para = False
    skip = 0
    for l in f:
        if l.find('<para>') >= 0:
            para = True
            s = u''
            continue
        if l.find('</para>') >= 0:
            para = False
            yield s
        if l.find('<!--') >= 0 and l.find('-->\n') >= 0:
            continue


        if l.find('<!--') >= 0:
            skip += 1
            continue
        if l.find('-->') >= 0:
            skip -= 1
            continue

        if has_ignore_tag_open(l):
            skip += 1
            continue
        if has_ignore_tag_close(l):
            skip -= 1
            continue

        if para and skip < 1:
            s = s + l.decode('utf-8')

def parse_paragraph(s):
    return re.sub('<[^>]+>', '', s.replace('\n', ''))

def parse_sgml(filename):
    f = open(filename)
    for p in get_paragraph(f):
#        print(p)
        pp = parse_paragraph(p)
        if pp:
            print(pp)
    f.close()

parse_sgml(sys.argv[1])

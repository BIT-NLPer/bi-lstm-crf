import numpy
import os, sys, codecs

s = []
label = []
out = codecs.open('dev.txt', 'w', 'gbk')
with codecs.open("dev.char.txt", 'r', 'utf-8') as f:
    for l in f.readlines():
        l = l.strip()zs
        if (l == ''):
            out.write(''.join(s))
            out.write(' ')
            out.write(label)
            out.write('\n')
            s.clear()
            label.clear()
            continue
        word, tag = l.split(' ')
        s.append(word)
        label.append(tag)

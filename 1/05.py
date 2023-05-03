# 05
# -*- coding: utf-8 -*-
import re

def bigram(wlist):
    word_bi_gram = []
    for i in range(len(wlist)-1):
        word_bi_gram.append(wlist[i]+',' +wlist[i+1])
    return word_bi_gram

w = 'I am an NLPer.'
w = re.sub('[,/.]','',w)
w1 = w.split(" ")
w2 = list(w)
print(bigram(w1),bigram(w2))
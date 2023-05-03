# 05
# -*- coding: utf-8 -*-
import re

def bigram(wlist):
    word_bi_gram = []
    for i in range(len(wlist)-1):
        word_bi_gram.append(wlist[i]+',' +wlist[i+1])
    return word_bi_gram

w_1 = 'paraparaparadise'
w_2 = 'paragraph'

X = set(bigram(list(w_1)))
Y = set(bigram(list(w_2)))

#和集合
def union_set(set1,set2):
    return set1|set2

#積集合
def intersection_set(set1,set2):
    return set1 & set2

#差集合
def differrence_set(set1,set2):
    return set1 - set2


print(union_set(X,Y))
print(intersection_set(X,Y))
print(differrence_set(X,Y))
print(('s,e' in intersection_set(X,Y)))
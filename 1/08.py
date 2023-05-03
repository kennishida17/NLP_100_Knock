# 00
# -*- coding: utf-8 -*-

def cipher(str):
    word_list = list(str)
    utf = []
    for word in word_list:
        if (97 <= ord(word) & ord(word) <= 122):
            utf.append(chr(219 - ord(word)))
        else:
            utf.append(word)
    
    print(''.join(utf))


cipher('the quick brown fox jumps over the lazy dog')


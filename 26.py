import numpy as np
import pandas as pd
import json
import gzip
import re

def read_wiki(fname,title):
    with gzip.open(fname,'rt') as f:
        for line in f:
            obj = json.loads(line)
            if obj['title']==title:
                return  obj['text']

# {{テンプレート名|テンプレート変数1=引数1|テンプレート変数2=引数2|....}}            
def get_basic_information(string):
    m1 = re.search(r'{{基礎情報 国.*?',string)
    print(m1.end())
    m2 = re.search(r'(.*)\n}}\n', string[m1.end():])
    return string[m1.end():m2.end()+1]

def set_basic_information(string):
    m = re.match(r'\|(.+)=(.*)', string)
    if m is None:
        return
    return {m.group(1):m.group(2)}

def remove_emphasis(string):
    #強調を除去
    m = re.match(r"(.*)('{3,5})(.*?)(\2)(.*)",string)
    if m is None:
        return string
    dst = m.group(1) + m.group(3) + m.group(5)
    return dst

def main():
    fname = 'jawiki-country.json.gz'
    text = read_wiki(fname, 'イギリス')
    print(len(text))
    text = get_basic_information(text).split('\n')

    basic_info = {}
    for line in text:
        line = line.replace("'''","")
        m = re.match(r'\|(.+)(=)(.*)', line)
        if m is None:
            continue
        val1 = remove_emphasis(m.group(3).strip())
        basic_info[m.group(1).strip()] = val1
    print(basic_info)



if __name__ == '__main__':
    main()
    
# [[File:ファイル名|thumb|ファイルの大きさ|説明]]
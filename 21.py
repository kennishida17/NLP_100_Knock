import numpy as np
import pandas as pd
import json
import gzip
import re

def read_wiki(fname,title):
    with gzip.open(fname,'r') as f:
        for line in f:
            obj = json.loads(line)
            if obj['title']==title:
                return  obj['text']
            
def is_category(string):
    #カテゴリー行を正規表現で判定
    return re.match(r'^\[\[Category:.+\]\]$',string)

def main():
    fname = 'jawiki-country.json.gz'
    text = read_wiki(fname,'イギリス').split('\n')

    #カテゴリの行を表示する
    for line in text:
        if is_category(line):
            print(line)

if __name__ == '__main__':
    main()
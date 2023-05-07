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
            

def is_file(string):
    return re.match(r'^\[\[:*(ファイル|File):.*\]\]$',string)

def get_file(string):
    m = re.match(r'^\[\[:*(ファイル|File):(.+?)\|.+\]\]$',string)
    return m.group(2)

def main():
    fname = 'jawiki-country.json.gz'
    text = read_wiki(fname,'イギリス').split('\n')

    #カテゴリ名を表示する
    for line in text:
        if is_file(line):
            print(get_file(line))


if __name__ == '__main__':
    main()
    
# [[File:ファイル名|thumb|ファイルの大きさ|説明]]
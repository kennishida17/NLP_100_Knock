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

def get_category_name(string):
    m =  re.match(r'^\[\[Category:(.*)\]\]$', string)
    return m.group(1).split('|')[0]

def is_section(string):
    return re.match(r'^=+.+=+$',string)

def get_section_level(string):
    m = re.match(r'^(=+)(.+?)=+$',string)
    return ' name : {0}\t level : {1}'.format(m.group(2), len(m.group(1))-1)

def main():
    fname = 'jawiki-country.json.gz'
    text = read_wiki(fname,'イギリス').split('\n')

    #カテゴリ名を表示する
    for line in text:
        if is_section(line):
            print(get_section_level(line))


if __name__ == '__main__':
    main()
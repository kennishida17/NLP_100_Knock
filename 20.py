import numpy as np
import pandas as pd
import json
import gzip

def read_wiki(fname,title):
    with gzip.open(fname,'r') as f:
        for line in f:
            obj = json.loads(line)
            if obj['title']==title:
                return  obj['text']

def main():
    fname = 'jawiki-country.json.gz'
    print(read_wiki(fname,'イギリス'))

if __name__ == '__main__':
    main()
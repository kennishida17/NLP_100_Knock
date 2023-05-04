import pandas as pd

df = pd.read_table('popular_names.txt',header=None,sep='\t',names=['name','sex','number','year'])
col1  = df['name']
print(len(set(col1)))
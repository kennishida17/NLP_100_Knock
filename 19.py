import pandas as pd

df = pd.read_table('popular_names.txt',header=None,sep='\t',names=['name','sex','number','year'])

vc = df['name'].value_counts()
print(vc)
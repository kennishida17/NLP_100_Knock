import pandas as pd

df = pd.read_table('popular_names.txt',header=None,sep='\t',names=['name','sex','number','year'])
df_sort = df.sort_values('number',ascending=False)
print(df_sort.head())
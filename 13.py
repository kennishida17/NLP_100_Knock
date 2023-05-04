import pandas as pd


# df = pd.read_table('popular_names.txt',header=None,sep='\t',names=['name','sex','number','year'])

df1 = pd.read_table('./col1.txt')
df2 = pd.read_table('./col2.txt')

#df1とdf2を結合
df1_df2 = pd.concat([df1,df2],axis=1)
#txtに出力
df1_df2.to_csv('col1_col2.txt',sep='\t',index=False)


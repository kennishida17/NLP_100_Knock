import pandas as pd

df = pd.read_table('popular_names.txt',header=None,sep='\t',names=['name','sex','number','year'])

def split_file(N):
  tmp = df.reset_index(drop=False)
  df_cut = pd.qcut(tmp.index, N, labels=[i for i in range(N)])
  df_cut = pd.concat([df, pd.Series(df_cut, name='sp')], axis=1)

  return df_cut

N = input('>> ')
df_cut = split_file(int(N))
df_cut['sp'].value_counts()
# print(df_cut.head(20))
# print(df_cut['sp'])


import numpy as np
import pandas as pd

#Missing data 
df = pd.DataFrame({'A': [1,2,np.nan],
				   'B': [5, np.nan, np.nan],
				   'C': [1,2,3]})
'''     
	 A    B  C
0  1.0  5.0  1
1  2.0  NaN  2
2  NaN  NaN  3 
'''
df.dropna()				#by default row
df.dropna(axis = 1)		#axis = 1 --> column 
df.dropna(thresh=2)		#rows with  >= 2 NA values are deleted
df.fillna(value = 'FILL VALUE')
 
df['A'].fillna(value = df['A'].mean(), inplace = True)
# print(df['A'])


#Group By 
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
'''
  Company   Person  Sales
0    GOOG      Sam    200
1    GOOG  Charlie    120
2    MSFT      Amy    340
3    MSFT  Vanessa    124
4      FB     Carl    243
5      FB    Sarah    350
'''
by_comp = df.groupby("Company")			#save object group-by in a new variable
# by_comp = by_comp.mean()				#mean, std, min, max, count, describe, transpose
by_comp = by_comp.describe().transpose()['GOOG']

'''
Sales  count      2.000000
       mean     160.000000
       std       56.568542
       min      120.000000
       25%      140.000000
       50%      160.000000
       75%      180.000000
       max      200.000000
Name: GOOG, dtype: float64
'''

#Merging, Joining, Concatenating 
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7]) 
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])

pd.concat([df1,df2,df3])

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})    
pd.merge(left,right,how='inner',on='key')

'''
	A	B	key	C	D
0	A0	B0	K0	C0	D0
1	A1	B1	K1	C1	D1
2	A2	B2	K2	C2	D2
3	A3	B3	K3	C3	D3
'''

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})

pd.merge(left, right, on=['key1', 'key2'])

'''
	A	B	key1	key2	C	D
0	A0	B0	K0		K0		C0	D0
1	A2	B2	K1		K0		C1	D1
2	A2	B2	K1		K0		C2	D2
'''

pd.merge(left, right, how='outer', on=['key1', 'key2'])
pd.merge(left, right, how='right', on=['key1', 'key2'])
pd.merge(left, right, how='left', on=['key1', 'key2'])
 
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])

left.join(right)
left.join(right, how='outer')


#Cool operations
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df['col2'].unique()
df['col2'].nunique()
df['col2'].value_counts() 
'''
444    2
555    1
666    1
'''

newdf = df[(df['col1']>2) & (df['col2']==444)]
def times2(x):
    return x*2

df['col1'].apply(times2)
del df['col1'] 		#permanent remove a column
df.columns			#get column names
df.index			#get index names
df.sort_values(by='col2') #inplace=False by default

#check for null
df.isnull()
df.dropna()			#Drop rows with NaN Values

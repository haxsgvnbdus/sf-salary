import numpy as np
import pandas as pd 
from numpy.random import randn


#SERIES

labels = ['a', 'b', 'c']
my_list = [10,20,30]
arr = np.array(my_list)

pdSeries = pd.Series(data = my_list)	#0    10
										#1    20
										#2    30
										#dtype: int64

labeled = pd.Series(data = my_list, index = labels)	#a    10
													#b    20
													#c    30
													#dtype: int64

obj = pd.Series(data = labels)		#0    a
									#1    b
									#2    c
									#dtype: object
ser1 = pd.Series(data = [1,2,3,4], index = ['USA', 'Germany', 'USSR', 'Japan'])
# print(ser1['USA'])

ser2 = pd.Series(data = [2,4,6,8], index = ['USA', 'Germany', 'Italy', 'Japan'])
# print(ser1+ser2)

#DATAFRAMES

np.random.seed(101)
df = pd.DataFrame(randn(5,4), index = 'A B C D E'.split(), columns = 'W X Y Z'.split())
'''
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
'''

Wcol = df['W']									#select COLUMN
WXcol = df[['W', 'X']]
Ycol = df.Y  									#SQL syntax not recommended
df['new'] = df['W'] + df['Y']					#create new column
df.drop('new', axis = 1, inplace = True)		#axis = 0 --> row, axis = 1 --> column
# print(df)										#inplace decides whether the removal applies to the original table

Arow = df.loc['A']								#select ROW
row2 = df.iloc[2]								#select ROW index
abwy = df.loc[['A','B'],['W','Y']]				#row A,B column W, Y
more0 = df[df > 0] 
more0columnW = df[df['W'] > 0]
s1 	= df[df['W'] > 0][['Y', 'X']]					#condition W > 0, show Y & Z
s2  = df[(df['W'] > 0) & (df['Y'] > 1)]				#& |

# print(df.reset_index())								#add index 0-len
new_ind = 'CA NY WY OR CO'.split() 
df['States'] = new_ind
df.set_index('States', inplace = True)


#Multi-index & Index hierarchy
outside = 'G1 G1 G1 G2 G2 G2'.split() 
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside, inside))				#[('G1', 1), ('G1', 2), ('G1', 3), ('G2', 1), ('G2', 2), ('G2', 3)]
hier_index = pd.MultiIndex.from_tuples(hier_index)  
		#MultiIndex(levels=[['G1', 'G2'], [1, 2, 3]],
        #			labels=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]])

df = pd.DataFrame(randn(6,2), index = hier_index, columns = ['A', 'B'])
'''
             A         B
G1 1  0.302665  1.693723
   2 -1.706086 -1.159119
   3 -0.134841  0.390528
G2 1  0.166905  0.184502
   2  0.807706  0.072960
   3  0.638787  0.329646
'''
everythingG1 = df.loc['G1']
df.index.names = ['Groups', 'Num']			#G1, G1 as groups, 1,2,3 as num
'''
                   A         B
Groups Num
G1     1    0.302665  1.693723
       2   -1.706086 -1.159119
       3   -0.134841  0.390528
G2     1    0.166905  0.184502
       2    0.807706  0.072960
       3    0.638787  0.329646
'''

g2_2_bcell = df.loc['G2'].loc[2]['B'] 

#cross section 
everythingG1 = df.xs('G1')
all1in2Gs = df.xs(1, level = 'Num')



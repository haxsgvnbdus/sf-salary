import numpy as np

my_list = [1,2,3]
arr = np.array(my_list)		#cast normal list to np array 

my_mat = [[1,2,3], [4,5,6], [7,8,9]]
arr2 = np.array(my_mat)
# print(arr2)

a = np.arange(0,10) 	#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = np.arange(0,11,2)	#[ 0,  2,  4,  6,  8, 10]
c = np.zeros(3) 		#[ 0.,  0.,  0.]
d = np.zeros((5,5))		#matrix 5x5 all values being 0
e = np.ones(3)		

f = np.linspace(0,10,4)		#return evenly spaced numbers over a specific interval 
							#3rd parameter: 4 meaning 3 space in between
g = np.eye(4)				#create identity matrix 4x4

#Random normal distribution rand/randn
h = np.random.rand(2)		#[ 0.11570539,  0.35279769] 
i = np.random.rand(5,5) 	
j = np.random.randint(1,100)	#44
k = np.random.randint(1,100,10)

l = np.arange(0,21)
l = l.reshape(7,3)			#returns an array containing the same data with a new shape

l.max()
l.argmax()
l.min()
l.argmin()

print("shape: {}".format(l.shape))
print("datatype: {}".format(l.dtype))

#indexing & selection 
import numpy as np


#tupla
arr = np.array([1, 2, 3, 4, 5])
# elenco
arr2 = np.array((1, 2, 3, 4, 5))

print(arr)




# matrice 0-d zero dimensioni
arr3 = np.array(42)

print(arr3)

# matrice 1-d zero dimensioni
arr4 = np.array([1, 2, 3, 4, 5])

print(arr4)

# matrice 2-d zero dimensioni
arr5 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr5)


# matrice 3-d zero dimensioni
arr6 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr6)
print(arr6.ndim)   # per sapere quante dimensioni ha un insieme 


# quella sarà la dimenzione massima del nostro insieme
arr7 = np.array([1, 2, 3, 4, 5], ndmin=1)

print(arr7)
print('number of dimensions :', arr7.ndim)
print(arr7[0])

print(arr7[2] + arr7[3])


arr8 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr8[0, 1])



arr9 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr9[0, 1, 2])
print(arr9[1, 1, 1 ])


from numpy import random

x = random.randint(100)

print(x)

# crea un array 1-D con 5 posizioni riempite con numeri random da 1 a 100
x2 =random.randint(100, size=(5))
print(x2)

x3 = random.randint(100, size=(3, 5))
print(x3)

# 

x = random.rand(5)

print(x)


x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)


x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)


print(type(np.add))

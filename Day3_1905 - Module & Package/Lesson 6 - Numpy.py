# Install Numpy ==> pip install numpy

# Import Numpy ==> import numpy as np
import numpy as np

# Numpy Array
listA = [1, 2, 3, 4]
arrayA = np.array(listA)
# print(arrayA)
# print(type(arrayA))

# Random Numpy

# Random float ==> np.random.random(size)
a = np.random.random(10)
# print(a)

# Random int :: randint(min, max, size)
b = np.random.randint(1, 10, 5)
# print(b)

# Arrange
c = np.arange(1, 10, 2)
# print(c)

# ReShape
arrayReshape = arrayA.reshape(2, 2)
# print(arrayReshape)


# NUMPY OPERATOR
""" array1 = np.arange(1, 10)
array2 = np.arange(10, 19)
array4 = array1 + array2
array5 = array1 - array2
array6 = array1 * array2
array7 = array1 / array2
array8 = array1 // array2
array9 = array1 ** array2
print(array4, array5, array6, array7, array8, array9, sep = "\n") """


# NUMPY INDEX

# NUMPY SORT
a = [[22221, 45, 26, 73], [3, 444, 16, 8], [4, 988222, 1251, 4547]]
a = np.array(a)
# print(a)
# print(a.shape)
# print(a.size)
""" print("-" * 10)
b = np.sort(a, axis=-1)
print(np.sort(a, axis = 1))
print(b) """

# Array Reshape & Transpose
""" np.random.seed(1)
k = np.random.randint(1, 19, (2, 3))
print(k)
k1 = np.reshape(k, (3, 2))
print(k1)
 """
#Array Transpose
# print(k.T)


# Array Concatenate
""" np.random.seed(0)
x = np.random.randint(10, 50, (4, 5))
y = np.random.randint(1, 10, (4, 5))
print(x)
print(y)
z = np.concatenate((x, y), axis=0)
print(z) """

# We can also use vstack, hstack to concatenate


#Split



#Broadcasting
""" a = np.array([1, 2, 3, 4])
b = np.array([2])
c = a + b
print(c) """

#Statistics
#Mean (Giá trị trung bình), Variance (Phương sai), Standard Deviation (Độ lệch chuẩn)
""" 
dog_height = np.array([600, 470, 170, 430, 300])
mean = np.mean(dog_height)
Standard_Deviation = np.std(dog_height)
print(mean)
print(Standard_Deviation)
variance = np.var(dog_height)
print(variance)
 """

#Sorting Arrays === np.sort
"""
np.sort(x) --> 
np.argsort()
"""
""" x = np.array([1, 33,444,8126317263,23,220])
y = np.sort(x, order= "DESC")
z = np.argsort(x)
print(y)
print(z)
 """

#Linear Algebra (Đại số tuyến tính)

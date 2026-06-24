import numpy as np

# Creating arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Array A:", a)
print("Array B:", b)

# Addition
print("\nAddition:")
print(a + b)

# Multiplication
print("\nElement-wise Multiplication:")
print(a * b)

# Matrix multiplication
matrix1 = np.array([[1, 2],
                    [3, 4]])

matrix2 = np.array([[5, 6],
                    [7, 8]])

print("\nMatrix Multiplication:")
print(matrix1 @ matrix2)

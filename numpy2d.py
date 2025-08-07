"""
This script contains code mucking about with 2 dimensional
numpy arrays >_<
"""

# Import necessary libraries
import numpy as np

# Convert following list to numpy array
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

A = np.array(a)

print("Numpy array A:\n", A)

# Get the array's size
print("The size of A is:", A.size)

# Access element on the first row and second collumn
print("Element in first row and second collumn of A is:", A[0, 1])

# Perform matrix multiplication with A and the following array B
B = np.array([[0, 1], [1, 0], [1, 1], [-1, 0]])

print("Numpy array B:\n", B)

C = np.dot(A, B)
print("A . B =\n", C)

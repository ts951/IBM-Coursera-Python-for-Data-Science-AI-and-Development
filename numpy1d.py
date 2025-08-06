"""
This script mucks about with 1 dimensional stuff in numpy for python
"""
# Fun fact! numpy sounds like a little goblin's name if you pronounce it numpee :O


# Import libraries! 
import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt

# Function to plot two vectors on a graph using matplotlib
def Plotvec2(a,b):
    ax = plt.axes()# to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)#Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)#Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)
    plt.show()

# Create an array and assign the value 20 to the second element
a = np.array([10, 2, 30, 40, 50])
print("Array was ", a)

a[1] = 20
print("Array is now", a)

# Print the even elements in the following array
a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("The even elements in ", a, " are:", a[1:8:2])

# Find and print the size, rank, and shape of the following array
a = np.array([10, 20, 30, 40, 50, 60, 70])
print("For array ", a, "\nSize = ", a.size, " Rank = ", a.ndim, " Shape = ", a.shape)

# Find and print the sum of the max and min values of the following array
a = np.array([-10, 201, 43, 94, 502])
sum = a.max() + a.min()
print("The sum of the maximum and minimum values of array ", a, " is ", sum)

# Add the following two arrays
a = np.array([10, 11, 12, 13, 14, 15])
b = np.array([20, 21, 22, 23, 24, 25])

print("The sum of ", a, " and ", b, " is ", a+b)

# Now subtract them!
print(a, " minus ", b, " is ", a-b)

# Now multiply these two!
a = np.array([10, 20, 30, 40, 50, 60])
b = np.array([2, 1, 2, 3, 4, 5])

print(a, " multiplied by ", b, " is ", a*b)

# Now divide a by a new one!
b = np.array([3, 5, 10, 8, 2, 33])

print(a, " divided by ", b, " is ", a/b)

# Get the dot product of these two
a = np.array([3, 5])
b = np.array([2, 4])

print("The dot product of ", a, " and ", b, " is ", np.dot(a, b))

# Add constant 5 to this array
a = np.array([1, 2, 3, -1])

print(a, " with the constant 5 added is ", a+5)

# Make a numpy array within 5 and 4 and with 6 elements using linspace
a = np.linspace(5, 4, num = 6)

print("Array with 6 elements from 5 to 4", a)

# Muliply -2 with the following numpy array
a = np.array([2, 4])

print(a, " multiplied by -2 is ", a*-2)

print("\n\n")

# Ok plot the following arrays as vectors using the function at the top
a = np.array([-1, 1])
b = np.array([1, 1])

Plotvec2(a, b)

# Dot product of these arrays
print("First dot product = ", np.dot(a, b))

# DO IT AGAIN

a = np.array([1, 0])
b = np.array([0, 1])

Plotvec2(a, b)

# Dot product of these two
print("Second dot product = ", np.dot(a, b))

# DO IT AGAIN

a = np.array([1, 1])
b = np.array([0, 1])

Plotvec2(a, b)

# Dot product of these final two
print("Third dot product = ", np.dot(a, b))

# Interesting to note above that only the third pair has a dot product that isn't 0 since they aren't perpendicular
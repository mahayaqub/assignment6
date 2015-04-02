#Question 1
# use numpy arrays to create the first 2-D array
# creates all the new specified arrays from the initial array

import numpy as np 

print ""
print "Printing results for Question 1"
print ""

# This command creates the initial array specified in the question
x = (np.arange(15).reshape(3,5) +1).transpose()
print 'x = '
print x

# This command extracts the second and fourth rows of the initial array
a = np.array([x[1],x[3]])
print 'a = '
print a

# Extract the second column of the initial array
b = x[:,1].reshape(5,1)
print 'b = '
print b

# Get the points between the rectangle indices given 
c = x[1:4,0:3]
print 'c = '
print c

# Get the values between 3 and 11 from the original array
d = x[np.where(x>3)]
print 'd = '
print d[np.where(d<11)]


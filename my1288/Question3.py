import numpy as np

#Question 3

print ""
print "Printing results for Question 3"
print ""

# create the 10x3 array of random numbers in the range [0,1]
Q3_random = np.random.rand(10,3)
print Q3_random

#create an array that can be used to compare which numbers are closest to 0.5
diff = np.absolute(Q3_random-0.5)

# takes the index of the numbers with the smallest absolute difference 
print Q3_random[np.where((diff - diff.min(axis=1).reshape(10,1))==0)]
import numpy as np 

#Question 2

print ""
print "Printing results for Question 2"
print ""

# create the main array that is required in the question
a2 = np.arange(25).reshape(5,5)

# you have to reshape the array that will be used as the divident 
b2 = np.array([1.,5,10,15,20]).reshape(5,1) 

# divide a2 by b2 directly as they are the right dimensions 
Q2_result = a2/b2
print Q2_result
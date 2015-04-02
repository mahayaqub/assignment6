import numpy as np
import matplotlib.pyplot as plt

#Question 4

print ""
print "Saving results for Question 4"
print ""

# create a Mandelbrot fractal

def MandelbrotFractal(N_max, some_threshold):

	x = np.linspace(-2, 1, 1000)
	y = np.linspace(-1.5, 1.5, 1000)

	# make an array that matches the x,y grid, since we want to store the img
	final_array = np.zeros((len(x),len(y)), dtype=bool) 

	# start a loop that will create the grid needed and will check all the conditions
	for i, x0 in enumerate(x):
		for j, y0 in enumerate(y):
			c = x0 + 1j*y0	# keep the initial value 
			z = c 		#value to be incremented

			for k in range(N_max):
				z = z**2 +c
				#check for the condition given in the question
				# changed the threshold given in the question and the operand so that the points that need to be bounded are included
				if np.absolute(z) > some_threshold:
					final_array[i, j] = True
					break
			else:
				final_array[i, j] = False

	plt.imshow(final_array.T, extent=[-2, 1, -1.5, 1.5])
	plt.gray()
	plt.savefig('mandelbrot_my1288.png')

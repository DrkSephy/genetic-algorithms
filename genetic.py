# -*- genetic.py -*-
# -*- MIT License (c) 2015 David Leonard -*-
# -*- drksephy.github.io -*-

# Implementation notes:
# 	* Each gene is composed of two equal length
# 	  lists, filled with elements randomly
# 	* Fitness function will be the closeness 
# 	  of the sum of the two lists
#   * Choose the surviving genes and cross them
#     over using the roulette method
#   * Repeat until convergence

import random
import pprint

# Generate a list of 100 random integers (no duplicates) 
# with range [1, 10000] exclusive
list = random.sample(range(1, 10000), 100)

# Complete population
population = []

def partition(list, size):
	"""
	Generates an initial population denoted by size using
	a list of data. 

	Parameters:
	    list: list
	    	- A List of numbers to form the base population with
	    size: integer 
	    	- The cardinality of the initial population to generate
	"""
	for i in range(0, size):
		subset = []
		# First population subset of 50
		subsetOne = []
		# Second population subset of 50
		subsetTwo = []
		# Generate a list of indices
		indices = [x for x in range(100)]
		# Shuffle the indices
	 	random.shuffle(indices)
	 	# Populate our lists
		for index in indices:
			# Randomly choose a subset to insert into
			choice = random.randint(0, 1)
			# We insert into the first subset
			if(choice == 0):
				if(len(subsetOne) == 50):
					# First subset is full, insert into second
					subsetTwo.append(list[index])
				else:
					# First subset has space, insert
					subsetOne.append(list[index])	
			else:
				if(len(subsetTwo) == 50):
					# Second subset is full, insert into first
					subsetOne.append(list[index])
				else:
					# Second subset has space, insert
					subsetTwo.append(list[index])

		# Append populations 
		subset.append(subsetOne)
		subset.append(subsetTwo)
		population.append(subset)

	return

partition(list, 20)
pprint.pprint(population)




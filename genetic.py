# -*- genetic.py -*-
# -*- MIT License (c) 2015 David Leonard -*-
# -*- drksephy.github.io -*-

import random

# Generate a list of 100 random integers (no duplicates) 
# with range [1, 10000] exclusive
list = random.sample(range(1, 10000), 100)
# First population subset of 50
subsetOne = []
# Second population subset of 50
subsetTwo = []

def partition(list):
	# Generate a list of indices
	indices = [x for x in range(100)]
	# Shuffle the indices
 	random.shuffle(indices)

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
			

	return

partition(list)

# At this point, but subsets should have a size of 50
print len(subsetOne)
print len(subsetTwo)




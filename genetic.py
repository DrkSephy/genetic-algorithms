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


# Partition method will operate on our initial list
# and randomly partition it into two subsets each 
# containing 50 integers, subsequently stored within
# subsetOne and subsetTwo.
def partition(list):
	# Generate a list of indices
	indices = [x for x in range(100)]
	print indices
	# Shuffle the indices
 	random.shuffle(indices)

	for index in indices:
		choice = random.randint(0, 1)
		print choice
		# We insert into the first subset
		if(choice == 0):
			# First subset isn't full
			if(len(subsetOne) - 1 != 50):
				subsetOne.append(list[index])
			else: 
				# First subset is full, insert into second
				subsetTwo.append(list[index])
		else:
			if(len(subsetTwo) - 1 != 50):
				subsetTwo.append(list[index])
			else:
				subsetOne.append(list[index])			
	return

partition(list)
# At this point, but subsets should have a size of 50
print len(subsetOne) - 1
print len(subsetTwo) - 1



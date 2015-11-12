# -*- genetic.py -*-
# -*- MIT License (c) 2015 David Leonard -*-
# -*- drksephy.github.io -*-

import random

# Generate a list of 100 random integers (no duplicates) 
# with range [1, 10000] exclusive
list = random.sample(range(1, 10000), 100)
print len(list)
# First population subset of 50
subsetOne = []
# Second population subset of 50
subsetTwo = []


# Partition method will operate on our initial list
# and randomly partition it into two subsets each 
# containing 50 integers, subsequently stored within
# subsetOne and subsetTwo.
def partition(list):
	while (len(subsetOne) < 50 and len(subsetTwo) < 50):
		# Select an array index from our initial list
		listChoice = random.randint(0, len(list) - 1)
		# Which subset should we randomly place value
		choice = random.randint(0, 1)
		if(choice == 0 and len(subsetOne) < 50):
			subsetOne.append(list[listChoice])
		elif(choice == 1 and len(subsetTwo) < 50):
			subsetTwo.append(list[listChoice])
	return

partition(list)
print subsetOne
print len(subsetOne)
print subsetTwo
print len(subsetTwo)



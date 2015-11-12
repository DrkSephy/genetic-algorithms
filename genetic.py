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
	return


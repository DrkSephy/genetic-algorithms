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
# Fitness of genes
populationFitness = []
# Frequency Table for convergence
frequency = {}

def partition(list, size):
	"""
	Generates an initial population denoted by size using
	a list of data. 

	Parameters:
	    list: list
	    	- A List of numbers to form the base population with
	    size: integer 
	    	- The cardinality of the initial population to generate
	Returns:
		list 
			- A list of comprised of two subsets of length 50
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

# For now, maybe a good fitness function is how many numbers
# the difference between the sets is less than. 
# For example, the following array of differences:
# 	[121, 12, 98, 75]
# 12 is lower than the other 3 members, so the fitness function 
# will assign a value of 3. The higher this number is, the better
# (closer to minimizing the sum)
def fitnessAssessment(population):
	"""
	Computes the fitness of each gene in our population. 

	Parameters: 
		population: list
			- The set of all genes 
	Returns:
		fitness: list
			- An array of fitness functions for our genes
	"""
	# Store differences between each gene
	differences = []
	
	# Compute differences between each gene
	for gene in population:
		difference = abs(sum(gene[0]) - sum(gene[1]))
		differences.append(difference)
	
	# Sort list of differences in ascending order
	sortedDifferences = sorted(differences)
	
	# Assign fitness to each gene based on how many 
	# other members a gene is less than
	for difference in sortedDifferences:
		fitness = len(sortedDifferences) - 1 - sortedDifferences.index(difference)
		# Append fitness of gene to a fitness list
		populationFitness.append(fitness)
		# Store fitness:difference 
		frequency[fitness] = difference

# Our initial population will consist of 20 genes (strings)
partition(list, 20)
# pprint.pprint(population)
fitnessAssessment(population)
# Check fitness values
print populationFitness	
print frequency




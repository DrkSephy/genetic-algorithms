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

#----------------------------------------
#       GENETIC ALGORITHM PARAMETERS     
#----------------------------------------

# Generate a list of 100 random integers (no duplicates) 
# with range [1, 10000] exclusive
list = random.sample(range(1, 10000), 100)

# Complete population
population = []

# Fitness of genes
populationFitness = []

# Frequency Table for convergence
frequency = {}

# Binary representation of population
binaryPopulation = []

#----------------------------------------
#            GENETIC OPERATORS     
#----------------------------------------

def mutation(population, rate):
	"""
	Performs a mutation on a given gene at a given probability rate.

	Parameters:
		population: list
			- List of all genes in our current population
		rate: float
			- Rate of mutation of a gene

	Returns:
	"""
	return

def crossover(first, second):
	"""
	Performs crossover of two genes using the roulette wheel selection.

	Parameters:
		first: list
			- The first subset gene to perform crossover with
		second: list
			- The second subset gene to perform crossover with

	Returns:

	"""
	return


#----------------------------------------
#             HELPER METHODS      
#----------------------------------------

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

def validateConversions(population, binary):
	"""
	Validates that each value in the population has the correct
	binary representation.

	Parameters:
		population: list
			- The list of genes consisting of arrays of integers
		binary: list
			- The list of genes in binary representation
	"""
	mismatch = False
	for gene in population:
		for subset in gene:
			for member in subset:
				if (member) != int(binary[population.index(gene)][gene.index(subset)][subset.index(member)], 2):
					print 'There was a mismatch!'
					mismatch = True
	print 'Values are identical'
	return mismatch 
					

def validateLength(binary, length):
	"""
	Validates that all members in binary representation are 
	correctly padded to have equal lengths.

	Parameters:
		binary: list
			- The binary representation of our population
		length: integer
			- The length that each member should be 
	"""
	lengthMismatch = False
	for gene in binary:
		for subset in gene:
			for member in subset:
				if len(member) != length:
					print 'There is a length mismatch among our population'
					lengthMismatch = True
	print 'Lengths are identical'
	return lengthMismatch



def convertToBinary(format, padding):
	"""
	Returns a binary representation of our population.

	Parameters:
		format: integer
			- How many characters to trim from result
		padding: integer
			- How many bits should be padded to result
	"""

	for gene in population:
		subset = []
		subsetOne = []
		subsetTwo = []
		for value in gene[0]:
			binary = bin(value)[format:].zfill(padding)
			subsetOne.append(binary)	
		for value in gene[1]:
			binary = bin(value)[format:].zfill(padding)
			subsetTwo.append(binary)
		subset.append(subsetOne)
		subset.append(subsetTwo)
		binaryPopulation.append(subset)

def incrementGeneration(generation):
	return generation + 1

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

def evaluateConvergence(frequency, convergence):
	"""
	Loops over frequency table and checks if we've reached 
	a value close to our convergence level.
	"""
	for key, value in frequency.iteritems():
		if value < convergence:
			print "We've reached a convergence value!"
			print "The gene: " + str(population[key]) + " has converged with a value of: " + str(value)
	return



# Our initial population will consist of 20 genes (strings)
partition(list, 20)
# pprint.pprint(population)
fitnessAssessment(population)
# Check fitness values
print populationFitness	
#print frequency
#evaluateConvergence(frequency, 500)
convertToBinary(2, 14)
#print population[0][0][0]
#print int(binaryPopulation[0][0][0], 2)
print(validateConversions(population, binaryPopulation))
print(validateLength(binaryPopulation, 14))




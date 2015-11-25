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

class Genetic(object):

	def __init__(self):

		# Generate a list of 100 random integers (no duplicates)
		# with range [1, 10000] exclusive
		self.list = random.sample(range(1, 10000), 100)

		# Complete population of binary strings
		self.population = []

		# Numerical representation of binary strings
		self.numericalPopulation = []

		# Fitness of genes
		self.populationFitness = []

		# Frequency Table for convergence
		self.frequency = {}

		# Binary representation of population
		self.binaryPopulation = []

		# Mutation rate = 1 / length of binary vector (14)
		self.mutationRate = 7.142857142857142

		# Fitness total
		self.fitnessSum = 0

	#----------------------------------------
	#            GENETIC OPERATORS
	#----------------------------------------

	def mutation(self, gene, rate):
		"""
		Performs a mutation on a given gene at a given probability rate.

		Parameters:
			gene: list
				- A gene consisting of a list of numbers to mutate
			rate: float
				- Rate of mutation of a gene
		"""

		mutatedGene = ''
		for subset in gene:
			for member in subset:
				for chromosome in member:
					mutationProbability = random.uniform(0, 100)
					if mutationProbability < rate:
						# Append mutated (toggled) bits
						mutatedGene += str(int(not int(chromosome)))
					else:
						mutatedGene += chromosome
				index = subset.index(member)
				subset[index] = mutatedGene
				mutated = False	
				mutatedGene = ''
		return

	def crossover(self, first, second):
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

	def selection(self, count, population):
		"""
		Selects the next set of strings that participate in the
		formation of the next population.

		Parameters:
			frequency - list
				- The entire population of genes
			count - integer
				- How many individuals we want to keep
		"""

		# Compute total fitness of population
		totalFitness = 0
		for key in self.frequency:
			totalFitness += key

		# Compute weighted fitnesses
		weightedFitness = [float(key) / float(totalFitness) for key in self.frequency]

		# Generate probability intervals
		probabilities = [round(sum(weightedFitness[:i + 1]) * 100, 2) for i in range(len(weightedFitness))]

		# Generate new population
		# NOTE: We might want to only return two individuals at a time
		# to pass into the crossover function. For now, we generate 
		# an entire new population which we will then randomly select 
		# two individuals each time to perform crossover with. 
		newPopulation = []
		for i in range(count):
			probability = random.uniform(0, 100)
			for (n, individual) in enumerate(population):
				if probability <= probabilities[n]:
					newPopulation.append(individual)
					break

		# Replace current population
		self.population = newPopulation
		return
		
	#----------------------------------------
	#             HELPER METHODS      
	#----------------------------------------

	def generatePopulation(self, size, length):
		"""
		Generates binary strings representing the initial population.

		Parameters:
			size: integer
				- How many binary strings to generate
			length: integer
				- Length of the binary string to be constructed
		"""
		binaryString = []
		for i in range(0, size):
			# Append 50 zeroes to string
			while(len(binaryString) < 50):
				binaryString.append('0')

			# Append 50 ones to string
			while(len(binaryString) < 100):
				binaryString.append('1')

			# Now shuffle the positions of zeros and ones
			random.shuffle(binaryString)

			# Join our new shuffled string
			shuffledString = ''.join(binaryString)

			# Append our string into our population
			self.population.append(shuffledString)
			binaryString = []
		return

	def validatePopulation(self):
		"""
		Tests whether all strings in our population adhere to 
		the invariant of having exactly 50 ones and 50 zeroes.
		"""
		for gene in self.population:
			if(gene.count('0') and gene.count('1') != 50):
				print 'Gene does not preserve invariant'
				break
		print 'Gene upholds invariant!'
		return


	def partition(self):
		"""
		Partitions a binary string into corresponding subsets. 
		"""
		
		for gene in self.population:
			subsetOne = []
			subsetTwo = []
			subset = []
			for (i, chromosome) in enumerate(gene):
				if chromosome == '0':
					subsetOne.append(self.list[i])
				if chromosome == '1':
					subsetTwo.append(self.list[i])
			subset.append(subsetOne)
			subset.append(subsetTwo)
			self.numericalPopulation.append(subset)
		return

	def validateConversions(self):
		"""
		Validates that each value in the population has the correct
		binary representation.

		Parameters:
			population: list
				- The list of genes consisting of arrays of integers
			binary: list
				- The list of genes in binary representation
		"""
					
	def fitnessAssessment(self, population):
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
			self.populationFitness.append(fitness)
			# Store fitness:difference 
			self.frequency[fitness] = difference
		return

	def evaluateConvergence(self, frequency, convergence):
		"""
		Loops over frequency table and checks if we've reached 
		a value close to our convergence level.
		"""
		for key, value in frequency.iteritems():
			if value < convergence:
				print "We've reached a convergence value!"
				print "The gene: " + str(population[key]) + " has converged with a value of: " + str(value)
		return

	#----------------------------------------
	#       	   MAIN FUNCTION     
	#----------------------------------------

	def main(self):
		# Generate population of 20 binary strings of length 100
		self.generatePopulation(20, 100)

		# Partition population of binary strings into respective subsets
		self.partition()

		# Generate fitness of each string
		self.fitnessAssessment(self.numericalPopulation)

		return

genetic = Genetic()
genetic.main()
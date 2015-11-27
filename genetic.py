# -*- genetic.py -*-
# -*- MIT License (c) 2015 David Leonard -*-
# -*- drksephy.github.io -*-

import random
import pprint
from prettytable import PrettyTable

class Genetic(object):

	def __init__(self):

		# Generate a list of 100 integers using an LCG
		self.list = self.linearCongruentialGenerator(5, 100, 3, 2, 10000)

		# Complete population of binary strings
		self.population = []

		# Numerical representation of binary strings
		self.numericalPopulation = []

		# Fitness of genes
		self.populationFitness = []

		# Frequency
		self.frequency =  {}

		# Binary representation of population
		self.binaryPopulation = []

		# Mutation rate = 1 / length of binary string (100)
		self.mutationRate = 1.0

		# Desired size of population
		self.populationSize = 20

		# Fitness total
		self.fitnessSum = 0

		# Current generation
		self.generation = 1

		# Track best fitness
		self.bestFitness = 999999999

		# Gather data on convergence 
		self.convergenceStats = []

	#----------------------------------------
	#            GENETIC OPERATORS
	#----------------------------------------

	def mutation(self, gene):
		"""
		Performs a mutation on a given gene at a given probability rate.

		Parameters:
			gene: string
				- A bit string to randomly mutate
			rate: float
				- Rate of mutation of a gene
		"""
		mutatedGene = ''
		mutatedOnes = 0
		mutatedZeroes = 0
		for chromosome in gene:
			mutationProbability = random.uniform(0, 100)
			if mutationProbability < self.mutationRate:
				mutatedGene += str(int(not int(chromosome)))
				if chromosome == '0':
					mutatedZeroes += 1
				else:
					mutatedOnes += 1
			else:
				mutatedGene += chromosome
		if mutatedOnes == mutatedZeroes:
			return mutatedGene
		else:
			return gene

	def crossover(self, count):
		"""
		Performs crossover of two genes using the roulette wheel selection.

		Parameters:
			first: list
				- The first gene to perform crossover with
			second: list
				- The second gene to perform crossover with
		"""
		newGeneration = []
		while len(newGeneration) < count:
			parentOne = self.selection(self.population)
			parentTwo = self.selection(self.population)
			successfulFirstChild = False
			successfulSecondChild = False
			while successfulFirstChild == False and successfulSecondChild == False:
				# Get a random crossover point
				crossoverPoint = random.randint(0, 99)

				# Check if we generate a first child correctly
				if successfulFirstChild == False:
					childOne = parentOne[0 : crossoverPoint + 1] + parentTwo[crossoverPoint + 1: 100]
					if self.validateGene(childOne):
						newGeneration.append(self.mutation(childOne))
						successfulFirstChild = True

				# Check if we generate a second child correctly
				if successfulSecondChild == False:
					childTwo = parentTwo[0 : crossoverPoint + 1] + parentOne[crossoverPoint + 1: 100]
					if self.validateGene(childTwo):
						newGeneration.append(self.mutation(childTwo))
						successfulSecondChild = True

		# Replace old population with new generation
		self.population = newGeneration

		# Increment generation counter
		self.generation += 1
		return

	def selection(self, population):
		"""
		Selects the next set of strings that participate in the
		formation of the next population.

		Parameters:
			frequency - list
				- The entire population of genes
		"""

		# Compute total fitness of population
		totalFitness = 0
		for key in self.frequency:
			totalFitness += key

		# Compute weighted fitnesses
		weightedFitness = [float(key) / float(totalFitness) for key in self.frequency]

		# Generate probability intervals
		probabilities = [round(sum(weightedFitness[:i + 1]) * 100, 2) for i in range(len(weightedFitness))]
		
		# Select an individual using weighted probabilities		
		probability = random.uniform(0, 100)
		for (n, individual) in enumerate(population):
			if probability <= probabilities[n]:
				return individual
		
	#----------------------------------------
	#             HELPER METHODS      
	#----------------------------------------

	def linearCongruentialGenerator(self, seed, count, a, c, m):
		numbers = []
		for i in xrange(count):
			seed = (a * seed + c) % m
			numbers.append(seed)
		return numbers

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

	def validateGene(self, gene):
		"""
		Tests whether a gene has an equal number of zeroes and ones. 
		"""
		if(gene.count('0') and gene.count('1') != 50):
			return False
		return True


	def partition(self):
		"""
		Partitions a binary string into corresponding subsets. 
		"""
		population = []
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
			population.append(subset)
		self.numericalPopulation = population
		return
					
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
		for (position, difference) in enumerate(sortedDifferences):
			fitness = len(sortedDifferences) - position - 1
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

	def frequencyTable(self):
		"""
		Initializes the frequency table.
		"""
		table = {}
		for i in range(0, 20):
			table[i] = []
		return table

	#----------------------------------------
	#       	 STATS FUNCTIONS
	#----------------------------------------
		
	def average(self, list):
		"""
		Returns the average out of a list of values.
		"""
		total = 0.0
		for value in list:
			total += float(value['generation'])
		return total / len(list)

	def median(self, list):
		"""
		Returns the median out of a list of values.
		"""
		values = []
		for item in list:
			values.append(float(item['generation']))
		sortedList = sorted(values)
		length = len(sortedList)
		if not length % 2:
			return (sortedList[length / 2] + sortedList[length / 2 - 1]) / 2.0
		return sortedList[length / 2]

	def maximum(self, list):
		"""
		Returns the maximum out of a list of values.
		"""
		values = []
		for item in list:
			values.append(float(item['generation']))
		return max(values)

	def range(self, list):
		"""
		Returns the range out of a list of values.
		"""
		values = []
		for item in list:
			values.append(float(item['generation']))
		return max(values) - min(values)

	def minimum(self, list):
		"""
		Returns the minimum out of a list of values.
		"""
		values = []
		for item in list:
			values.append(float(item['generation']))
		return min(values)

	#----------------------------------------
	#       	  MAIN FUNCTION
	#----------------------------------------

	def main(self):
		for i in xrange(0, 9):
			# Clear existing population
			self.population = []

			# Clear existing best fitness
			self.bestFitness = 999999999

			# Numerical representation of binary strings
			self.numericalPopulation = []

			# Fitness of genes
			self.populationFitness = []

			# Frequency
			self.frequency = {}

			# Binary representation of population
			self.binaryPopulation = []

			# Desired population size
			self.populationSize = 20

			# Fitness total
			self.fitnessSum = 0			

			# Generate inital population of 20 binary strings of length 100
			self.generatePopulation(self.populationSize, 100)

			# Set generation counter to 1
			self.generation = 1

			self.mutationRate = 1.0

			# Run genetic algorithm until convergence
			while self.generation < 10000:
				# Log generation being tested
				print 'Processing generation: ' + str(self.generation)
	
				# Partition new generation of genes
				self.partition()

				# Compute fitness of each new gene
				self.fitnessAssessment(self.numericalPopulation)
				
				if self.generation == 10000:
					statistics = {}
					statistics['generation'] = self.generation
					statistics['value'] = self.bestFitness
					statistics['iteration'] = i
					self.convergenceStats.append(statistics)
				else: 
					if self.frequency[len(self.frequency) - 1] < self.bestFitness:
						self.bestFitness = self.frequency[len(self.frequency) - 1]
						if self.bestFitness < 5:
							statistics = {}
							statistics['generation'] = self.generation
							statistics['value'] = self.bestFitness
							statistics['iteration'] = i
							self.convergenceStats.append(statistics)
							break				

				# Select 10 weighted strings to form new population with
				self.selection(self.population)		

				# Perform crossover to form a new generation
				self.crossover(self.populationSize)	

		table = PrettyTable()
		x = PrettyTable(["Statistic", "Generation Count", "Convergence Value", "Mutation Rate", "Population Size"])
		x.padding_width = 1
		x.add_row(["Min", self.minimum(self.convergenceStats), 0, self.mutationRate, self.populationSize])
		x.add_row(["Max", self.maximum(self.convergenceStats), 0, self.mutationRate, self.populationSize])
		x.add_row(["Med", self.median(self.convergenceStats),  0, self.mutationRate, self.populationSize])
		x.add_row(["Rng", self.range(self.convergenceStats),   0, self.mutationRate, self.populationSize])
		x.add_row(["Avg", self.average(self.convergenceStats), 0, self.mutationRate, self.populationSize])
		print x

		return

# Instantiate class
genetic = Genetic()

# Run algorithm
genetic.main()
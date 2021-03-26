import random

processing_time = {
    'J1': 15,
    'J2': 20,
    'J3': 20,
    'J4': 10,
    'J5': 30,
    'J6': 5,
    'J7': 15,
    'J8': 40,
}

deadline = {
    'J1': 20,
    'J2': 40,
    'J3': 60,
    'J4': 30,
    'J5': 70,
    'J6': 20,
    'J7': 50,
    'J8': 80,
}

# Intializing the population size of 100
POPULATION_SIZE = 10

# Created GENES which contains every possible character for our solution.
GENES = ['J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8']

# Intilizing the start Time
start_time = 0


# Created A class to define a chromosome with its fitness function.
class Individual:
    # Initialzing the chromosome and fitness function
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calculateFitness()

    # Calculating Fitness of the chromosome.
    def calculateFitness(self):
        fitness = 0
        start = 0
        for i in range(len(self.chromosome)):
            fitness += abs(start + processing_time[self.chromosome[i]] - deadline[self.chromosome[i]])
            start = start+processing_time[self.chromosome[i]]
        return fitness


# Creating a random GENE
def mutateGenes():
    return random.choice(GENES)


# Intializing a population with random GENES
def createGNOME():
    GNOME = []
    while len(GNOME) != len(GENES):
        x = mutateGenes()
        if x not in GNOME:
            GNOME.append(x)
    return GNOME


# Initialing the whole Population
def initializePopulation():
    population = []  # Empty Population Array
    for _ in range(POPULATION_SIZE):
        gnome = createGNOME()
        # Creating GENES
        population.append(Individual(gnome))

    return population


# Generating new population
def selectionReproduction(population):
    # Sorting the population according to fitness function.
    population = sorted(population, key=lambda x: x.fitness)

    new_generation = []
    # Taking The Intial 10% of fitest population to the next generation
    new_generation.extend(population[:int(0.1 * POPULATION_SIZE)])

    # Crossing Over 90% of GENES with each other.
    for _ in range(int(0.9 * POPULATION_SIZE)):
        parent1 = random.choice(population[:POPULATION_SIZE // 2])
        parent2 = random.choice(population[:POPULATION_SIZE // 2])
        # Cross over two GENES
        child = crossover(parent1, parent2)
        # Mutating the child to generate new Possibility.
        mutated_child = mutation(child)
        new_generation.append(mutated_child)

    # returning the new genaration population.
    return new_generation


# Doing the Uniform crossover.
def crossover(chromosome1, chromosome2):
    child_chromosome = []
    for i in range(len(GENES)):
        # Calculating the random probability.
        prob = random.random()

        # if Probability belongs to less than 50%, then consider 1st Chromosome GENE.
        if prob < 0.50 and chromosome1.chromosome[i] not in child_chromosome:
            child_chromosome.append(chromosome1.chromosome[i])
        # if Probability belongs to greater than 50%, then consider 2nd Chromosome GENE.
        elif prob > 0.5 and chromosome2.chromosome[i] not in child_chromosome:
            child_chromosome.append(chromosome2.chromosome[i])

    # Incase length lesser than required length than appending some random GENES
    while len(child_chromosome) < len(GENES):
        gene = mutateGenes()
        if gene not in child_chromosome:
            child_chromosome.append(gene)

    return Individual(child_chromosome)


# Doing A Random Mutation.
def mutation(chromosome):
    child_chromosome = chromosome.chromosome
    while True:
        # Mutating two random gene to generate new possibility.
        a = random.randint(0, len(GENES)-1)
        b = random.randint(0, len(GENES)-1)
        if a != b:
            # Swapping Two Random GENE of Chromosome.
            child_chromosome[a], child_chromosome[b] = child_chromosome[b], child_chromosome[a]
            break
    return Individual(child_chromosome)


# Displaying The output.
generation = 1
population = initializePopulation()

# Displaying GENES and Its Fitness funtion till its fitness function reaches 0.
while True:
    population = selectionReproduction(population)

    # Mininmum Value of Fitness function That can be achived in this is 175(HardCoding)
    if population[0].fitness == 175:
        break

    print("Generation: {}   String: {}  Fitness: {}".format(generation, " ".join(population[0].chromosome),
                                                            population[0].fitness))
    generation += 1

print("Generation: {}   String: {}  Fitness: {}".format(generation, " ".join(population[0].chromosome),
                                                        population[0].fitness))

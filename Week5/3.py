import random

n = int(input("Enter The Number of positive integer value:\n"))
w = [i for i in range(1, n + 1)]
TARGET = int(input("Enter The Amount:\n"))
MAXIMUM_NUMBER_OF_COINS = TARGET // n
GENES = [i for i in range(MAXIMUM_NUMBER_OF_COINS + 1)]

POPULATION_SIZE = 100


class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calculateFitness()
        self.coins = self.numberOfCoins()

    def calculateFitness(self):
        add = 0
        for i in range(len(w)):
            add += w[i] * self.chromosome[i]

        return abs(TARGET - add)

    def numberOfCoins(self):
        num = 0
        for i in self.chromosome:
            num += i

        return num


def mutateGenes():
    return random.choice(GENES)


def createGNOME():
    return sorted([mutateGenes() for _ in range(n)])


def initializePopulation():
    population = []
    for _ in range(POPULATION_SIZE):
        population.append(Individual(createGNOME()))

    return population


def selectiveReproduction(population):
    population = sorted(population, key=lambda x: x.fitness)

    i = 0
    while population[i].fitness == 0:
        i += 1

    population[:i] = sorted(population[:i], key=lambda x: x.coins)
    new_generation = []
    new_generation.extend(population[:int(0.1 * POPULATION_SIZE)])
    for _ in range(int(0.9 * POPULATION_SIZE)):
        parent1 = random.choice(population[:POPULATION_SIZE // 2])
        parent2 = random.choice(population[:POPULATION_SIZE // 2])
        child_chromosome = crossover(parent1, parent2)
        mutate_child = mutation(child_chromosome)
        new_generation.append(mutate_child)

    return new_generation


def crossover(chromosome1, chromosome2):
    child_chromosome = []
    for i in range(n):
        prob = random.random()
        if prob < 0.5:
            child_chromosome.append(chromosome1.chromosome[i])
        else:
            child_chromosome.append(chromosome2.chromosome[i])
    child_chromosome.sort()
    return Individual(child_chromosome)


def mutation(chromosome):
    child_chromosome = []
    for i in range(len(chromosome.chromosome)):
        prob = random.random()
        if prob >= 0.9 or prob <= 0.1:
            child_chromosome.append(mutateGenes())
        else:
            child_chromosome.append(chromosome.chromosome[i])
    child_chromosome.sort()
    return Individual(child_chromosome)


generation = 1
population = initializePopulation()

while True:
    population = selectiveReproduction(population)

    if population[0].fitness == 0:
        break

    print("Generation: {} \nString: {}  \nFitness: {}\n".format(generation, population[0].chromosome,
                                                                population[0].fitness))
    generation += 1

print("Generation: {}  \nString: {}  \nFitness: {}".format(generation, population[0].chromosome, population[0].fitness))

import random

POPULATION_SIZE = 100

GENES = '''qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZCVBNM 123456890'''
TARGET = "I love GeeksForGeeks"


class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calculateFitness()

    def calculateFitness(self):
        global TARGET
        fitness = 0
        for ch1, ch2 in zip(self.chromosome, TARGET):
            if ch1 != ch2:
                fitness += 1
        return fitness


def mutateGenes():
    return random.choice(GENES)


def createGNOME():
    return [mutateGenes() for _ in range(len(TARGET))]

def initializePopulation():
    population = []
    for _ in range(POPULATION_SIZE):
        gnome = createGNOME()
        population.append(Individual(gnome))

    return population


def selectionReproduction(population):
    population = sorted(population, key=lambda x: x.fitness)

    new_generation = []
    new_generation.extend(population[:int(0.1 * POPULATION_SIZE)])

    for _ in range(int(0.9 * POPULATION_SIZE)):
        parent1 = random.choice(population[:POPULATION_SIZE//2])
        parent2 = random.choice(population[:POPULATION_SIZE//2])
        child = crossover(parent1, parent2)
        mutated_child = mutation(child)
        new_generation.append(mutated_child)

    return new_generation


def crossover(chromosome1, chromosome2):
    child_chromosome = []
    for i in range(len(chromosome1.chromosome)):
        prob = random.random()

        if prob < 0.50:
            child_chromosome.append(chromosome1.chromosome[i])
        else:
            child_chromosome.append(chromosome2.chromosome[i])

    return Individual(child_chromosome)


def mutation(chromosome):
    child_chromosome = []
    for i in range(len(chromosome.chromosome)):
        prob = random.random()
        if prob >= 0.9 or prob <= 0.1:
            child_chromosome.append(mutateGenes())
        else:
            child_chromosome.append(chromosome.chromosome[i])

    return Individual(child_chromosome)


generation = 1
population = initializePopulation()

while True:
    population = selectionReproduction(population)

    if population[0].fitness == 0:
        break

    print("Generation: {}   String: {}  Fitness: {}".format(generation, "".join(population[0].chromosome), population[0].fitness))
    generation += 1

print("Generation: {}   String: {}  Fitness: {}".format(generation, "".join(population[0].chromosome), population[0].fitness))

import random

N = 10
GENES = [i for i in range(1, N + 1)]

TARGET_SUM = 36
TARGET_PRO = 360
TARGET_SIZE = N // 2

POPULATION_SIZE = 100


class Individual:
    def __init__(self, pile1, pile2):
        self.pile1 = pile1
        self.pile2 = pile2
        self.fitness = self.calculateFitness()

    def calculateFitness(self):
        sumOfPile1 = 0
        for i in self.pile1:
            sumOfPile1 += i

        prodOfPile2 = 1
        for i in self.pile2:
            prodOfPile2 *= i

        return abs(sumOfPile1 - TARGET_SUM), abs(prodOfPile2 - TARGET_PRO)


def mutateGenes():
    return random.choice(GENES)


def createGNOME():
    pile1 = [mutateGenes() for _ in range(TARGET_SIZE)]
    pile2 = []
    for i in GENES:
        if i not in pile1:
            pile2.append(i)

    return pile1, pile2


def initializePopulation():
    population = []
    for _ in range(POPULATION_SIZE):
        gnome_pile1, gnome_pile2 = createGNOME()
        population.append(Individual(gnome_pile1, gnome_pile2))

    return population


def selectionReproduction(population):
    population = sorted(population, key=lambda x: x.fitness[0] + x.fitness[1])

    new_generation = []
    new_generation.extend(population[:int(0.1 * POPULATION_SIZE)])

    for _ in range(int(0.9 * POPULATION_SIZE)):
        parent1 = random.choice(population[:POPULATION_SIZE // 2])
        parent2 = random.choice(population[:POPULATION_SIZE // 2])
        child = crossover(parent1, parent2)
        mutated_child = mutation(child)
        new_generation.append(mutated_child)

    return new_generation


def crossover(chromosome1, chromosome2):
    child_chromosome_pile1 = []
    for i in range(len(chromosome1.pile1)):
        prob = random.random()

        if prob < 0.50 and chromosome1.pile1[i] not in child_chromosome_pile1:
            child_chromosome_pile1.append(chromosome1.pile1[i])
        elif prob >= 0.5 and chromosome2.pile1[i] not in child_chromosome_pile1:
            child_chromosome_pile1.append(chromosome2.pile1[i])

    while len(child_chromosome_pile1) < TARGET_SIZE:
        gene = mutateGenes()
        if gene not in child_chromosome_pile1:
            child_chromosome_pile1.append(gene)

    child_chromosome_pile2 = []
    for i in GENES:
        if i not in child_chromosome_pile1:
            child_chromosome_pile2.append(i)

    return Individual(child_chromosome_pile1, child_chromosome_pile2)


def mutation(chromosome):
    child_chromosome_pile1, child_chromosome_pile2 = chromosome.pile1, chromosome.pile2
    rand = random.randint(0, TARGET_SIZE-1)
    child_chromosome_pile1[rand], child_chromosome_pile2[rand] = child_chromosome_pile2[rand], child_chromosome_pile1[rand]

    return Individual(child_chromosome_pile1, child_chromosome_pile2)


generation = 1
population = initializePopulation()

while True:
    population = selectionReproduction(population)

    if population[0].fitness[0] == 0 and population[0].fitness[1]==0:
        break

    print("Generation: {} \nString:\nPile1 {}\nPile2 {}  \nFitness: {}\n".format(generation, population[0].pile1, population[0].pile2, population[0].fitness))
    generation += 1

print("Generation: {}  \nString:\nPile1 {}\nPile2 {}  \nFitness: {}".format(generation, population[0].pile1, population[0].pile2, population[0].fitness))

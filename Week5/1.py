import random

POPULATION_SIZE = 100

V = int(input("Enter Vertex:"))
GENES = "".join([str(i) for i in range(V)])


class Individual:
    def __init__(self, chromsome):
        self.chromosome = chromsome
        self.fitness = self.calculateFitness()

    def calculateFitness(self):
        global graph
        fitness = 0

        for i in range(len(self.chromosome) - 1):
            if graph[self.chromosome[i]][self.chromosome[i + 1]] == -1:
                return 999999
            else:
                fitness += graph[self.chromosome[i]][self.chromosome[i + 1]]
        return fitness


def mutateGenes():
    return int(random.choice(GENES))


def createGNOME():
    gnome = [0]
    while len(gnome) != V:
        gene = mutateGenes()
        if gene not in gnome:
            gnome.append(gene)

    gnome.append(gnome[0])
    return gnome


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
        parent1 = random.choice(population[:POPULATION_SIZE // 2])
        parent2 = random.choice(population[:POPULATION_SIZE // 2])
        child = crossover(parent1, parent2)
        mutated_child = mutation(child)
        if mutated_child.fitness<=population[0].fitness:
            new_generation.append(mutated_child)

    return new_generation


def crossover(chromosome1, chromosome2):
    child_chromosome = []
    for i in range(V):
        prob = random.random()

        if prob < 0.50 and chromosome1.chromosome[i] not in child_chromosome:
            child_chromosome.append(chromosome1.chromosome[i])
        elif prob >= 0.5 and chromosome2.chromosome[i] not in child_chromosome:
            child_chromosome.append(chromosome2.chromosome[i])

    while len(child_chromosome) < V:
        gene = mutateGenes()
        if gene not in child_chromosome:
            child_chromosome.append(gene)

    while len(child_chromosome) < V:
        gene = mutateGenes()
        if gene not in child_chromosome:
            child_chromosome.append(gene)

    child_chromosome.append(child_chromosome[0])
    return Individual(child_chromosome)


def mutation(chromosome):
    child_chromosome = chromosome.chromosome
    while True:
        a = random.randint(1, V - 1)
        b = random.randint(1, V - 1)
        if a != b:
            child_chromosome[a], child_chromosome[b] = child_chromosome[b], child_chromosome[a]
            break
    return Individual(child_chromosome)


graph = []
for i in range(V):
    graph.append(list(map(int, input().split())))

# graph = [[0, 2, -1, 12, 5],
#          [2, 0, 4, 8, -1],
#          [-1, 4, 0, 3, 3],
#          [12, 8, 3, 0, 10],
#          [5, -1, 3, 10, 0]]

generation = 1
population = initializePopulation()

while generation < 10:
    population = selectionReproduction(population)

    print("Generation: {}   String: {}  Fitness: {}".format(generation, population[0].chromosome,
                                                            population[0].fitness))
    generation += 1

print("Generation: {}   String: {}  Fitness: {}".format(generation, population[0].chromosome,
                                                        population[0].fitness))

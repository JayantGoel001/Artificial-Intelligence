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
    gnome = []
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
        new_generation.append(mutated_child)

    return new_generation


def crossover(chromosome1, chromosome2):
    child_chromosome = [" "]*(V+1)

    rand = random.randint(1, V-1)

    child_chromosome[:rand] = chromosome1[:rand]
    child_chromosome[rand:] = chromosome2[rand:]

    child_chromosome[V] = child_chromosome[0]

    for i in range(V):
        pass


    return Individual(child_chromosome)


def mutation(chromosome):
    child_chromosome = chromosome.chromosome
    while True:
        a = random.randint(0, V)
        b = random.randint(0, V)
        if a != b:
            child_chromosome[a], child_chromosome[b] = child_chromosome[b], child_chromosome[a]
            break
        child_chromosome[V] = child_chromosome[0]
    return Individual(child_chromosome)


graph = []
for i in range(V):
    graph.append(list(map(int, input().split())))

generation = 1
population = initializePopulation()

while generation < 1000:
    population = selectionReproduction(population)
    print("Generation: {}   String: {}  Fitness: {}".format(generation, population[0].chromosome,
                                                            population[0].fitness))
    generation += 1

print("Generation: {}   String: {}  Fitness: {}".format(generation, population[0].chromosome,
                                                        population[0].fitness))

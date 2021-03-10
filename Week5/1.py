import random

POPULATION_SIZE = 100

V = int(input("Enter Vertex:"))
GENES = "".join([i for i in range(V)])


class Individual:
    def __init__(self, chromsome):
        self.chromosome = chromsome
        self.graph = self.graph or []
        self.fitness = self.calculateFitness()

    def setGraph(self, graph):
        self.graph = graph

    def calculateFitness(self):
        fitness = 0

        for i in range(len(self.chromosome) - 1):
            if self.graph[i][i + 1] != -1:
                return -1
            else:
                fitness += self.graph[i][i + 1]
        return fitness


def mutateGenes():
    return random.choice(GENES)


def createGNOME():
    return [mutateGenes() for _ in range(len(V))]


def initializePopulation():
    population = []
    for _ in range(POPULATION_SIZE):
        gnome = createGNOME()
        population.append(Individual(gnome))

    return population


def selectionReproduction(population):
    return sorted(population, key=lambda x: x.fitness)


def crossover(chromosome1, chromosome2):
    child_chromosome = []
    for i in range(len(chromosome1.chromosome)):
        prop = random.random()
        if prop < 0.5:
            child_chromosome.append(chromosome1.chromosome)
        else:
            child_chromosome.append(chromosome2.chromosome)

    return Individual(child_chromosome)


def muatation(chromosome):
    child_chromosome = []
    for i in range(len(chromosome.chromsome)):
        prob = random.random()
        if prob >= 0.9 or prob < 0.1:
            child_chromosome.append(mutateGenes())
        else:
            child_chromosome.append(chromosome.chromsome[i])
    return Individual(child_chromosome)


graph = []
for i in range(V):
    graph.append([])
    for j in range(V):
        graph[i].append(int(input()))

generation = 1
population = initializePopulation()

while True:
    population = selectionReproduction(population)


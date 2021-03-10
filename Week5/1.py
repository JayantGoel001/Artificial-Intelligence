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



graph = []
for i in range(V):
    graph.append([])
    for j in range(V):
        graph[i].append(int(input()))

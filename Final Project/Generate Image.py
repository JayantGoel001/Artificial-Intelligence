import random
import sys
import cv2
import numpy as np

if len(sys.argv) < 4:
    print("More than 3 arguments required")
    sys.exit(0)

img_path = sys.argv[1]
POPULATION_SIZE = int(sys.argv[2])
max_generations = int(sys.argv[3])

image = cv2.imread(img_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
width, height, _ = image.shape

TARGET_IMAGE = image.flatten()
TARGET_SIZE = TARGET_IMAGE.shape[0]
minValue = min(TARGET_IMAGE)
maxValue = max(TARGET_IMAGE)

class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calculateFitness()

    def calculateFitness(self):
        return np.sum(np.abs(self.chromosome - TARGET_IMAGE))


def mutateGenes():
    return random.randint(minValue, maxValue)


def createGNOME():
    return [mutateGenes() for _ in range(TARGET_SIZE)]


def initializePopulation():
    population = []
    for _ in range(POPULATION_SIZE):
        population.append(Individual(createGNOME()))

    return population


def selectiveReproduction(population):
    population = sorted(population, key=lambda x: x.fitness)

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
    for i in range(TARGET_SIZE):
        prob = random.random()
        if prob < 0.5:
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


generation = 0
population = initializePopulation()

while generation <= max_generations:
    print("Current Generation :", generation)
    population = selectiveReproduction(population)

    if population[0].fitness == 0:
        generated_image = np.asarray(population[0].chromosome).reshape(width, height, 3)
        cv2.imwrite("Ultimate image.jpg", generated_image)
        break

    if generation % int(0.1 * max_generations) == 0:
        generated_image = np.asarray(population[0].chromosome).reshape(width, height, 3)
        cv2.imwrite("generated image {}.jpg".format(generation), generated_image)
        print("Generated Image saved with fitness value", population[0].fitness)
    generation += 1

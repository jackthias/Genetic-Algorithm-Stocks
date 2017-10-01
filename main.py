from math import ceil

from breeding import selection, crossover, mutation
import constants
from fitness import check_fitness
from population import create_population


class Output:
    def __init__(self, current_population: list):
        current_population.sort(key=lambda member: check_fitness(member))
        self.max = (population[-1], check_fitness(population[-1]))
        self.min = (population[0], check_fitness(population[0]))
        mid = ceil(len(current_population) / 2)
        self.median = (population[mid], check_fitness(population[mid]))
        fitness_sum = 0
        for member in current_population:
            fitness_sum += check_fitness(member)
        self.mean = fitness_sum / len(current_population)

    def __str__(self):
        return "MAX: {}\nMIN: {}\nMEDIAN: {}\nMEAN: {}".format(self.max[1], self.min[1], self.median[1], self.mean)


population = create_population(constants.POPULATION_SIZE)
breeding_pool_size = int(constants.POPULATION_SIZE * constants.PERCENTAGE_SURVIVAL)

for i in range(0, constants.NUMBER_OF_GENERATIONS):
    if i % constants.DISPLAY_INTERVALS == 0:
        print(str(Output(population)))
    breeding_pool = selection(constants.ELITIST_SELECTION, population, breeding_pool_size)
    population = crossover(constants.UNIFORM_CROSSOVER, breeding_pool, constants.POPULATION_SIZE)
    mutation(population, constants.CHANCE_OF_MUTATION)
print(str(Output(population)))

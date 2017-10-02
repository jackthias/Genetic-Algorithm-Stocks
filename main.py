from math import ceil

import plotly
import plotly.plotly as py
import plotly.graph_objs as go

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
        for pop_member in current_population:
            fitness_sum += check_fitness(pop_member)
        self.mean = fitness_sum / len(current_population)

    def __str__(self):
        return "MAX: {}\nMIN: {}\nMEDIAN: {}\nMEAN: {}".format(self.max[1], self.min[1], self.median[1], self.mean)

if constants.VISUALIZATION_ACTIVE:
    cred_file = open(constants.CREDENTIAL_FILENAME, 'r')
    cred_file_data = cred_file.readlines()
    credentials = []
    for line in cred_file_data:
        credentials.append(line[:-1])
    plotly.tools.set_credentials_file(username=credentials[0], api_key=credentials[1])

    population = create_population(constants.POPULATION_SIZE)
    breeding_pool_size = int(constants.POPULATION_SIZE * constants.PERCENTAGE_SURVIVAL)

    max_values = []
    median_values = []
    mean_values = []

for i in range(0, constants.NUMBER_OF_GENERATIONS):
    if constants.VISUALIZATION_ACTIVE:
        population.sort(key=lambda member: check_fitness(member))
        max_values.append(check_fitness(population[-1]))
        mid = ceil(len(population) / 2)
        median_values.append(check_fitness(population[mid]))
        fit_sum = 0
        for pop_member in population:
            fit_sum += check_fitness(pop_member)
        mean_values.append(fit_sum / len(population))
    if i % constants.DISPLAY_INTERVALS == 0 and constants.TEXT_OUTPUT:
        print("Generation {}:".format(i))
        print(str(Output(population)))
        print()
    breeding_pool = selection(constants.ELITIST_SELECTION, population, breeding_pool_size)
    population = crossover(constants.UNIFORM_CROSSOVER, breeding_pool, constants.POPULATION_SIZE)
    mutation(population, constants.CHANCE_OF_MUTATION)

if constants.VISUALIZATION_ACTIVE:
    x_range = range(0, constants.NUMBER_OF_GENERATIONS)
    x_range = list(x_range)
    max_trace = go.Scatter(
        x=x_range,
        y=max_values,
        name='Max'
    )
    median_trace = go.Scatter(
        x=x_range,
        y=median_values,
        name='Median'
    )
    mean_trace = go.Scatter(
        x=x_range,
        y=mean_values,
        name='Mean'
    )

    data = [max_trace, median_trace, mean_trace]
    layout = dict(title='Fitness over Generations',
                  xaxis=dict(title='Generation'),
                  yaxis=dict(title='Fitness in Terms of U.S. Dollars Gained'))
    fig = dict(data=data, layout=layout)
    py.plot(fig, filename='genetic-stock-graph')

print("Final Generation:")
print(str(Output(population)))

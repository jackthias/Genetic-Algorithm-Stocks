import random
from chromosome import make_chromosome

standard_var = 1.15
mean = 0


def get_high_low():
    return random.normalvariate(mean, standard_var)


def get_buy_short():
    return random.choice([True, False])


def random_chromosome():
    return make_chromosome(get_high_low(), get_high_low(), get_high_low(), get_high_low(), get_buy_short())


def create_population(n):
    population = list()
    for _ in range(0, n):
        population.append(random_chromosome())
    return population
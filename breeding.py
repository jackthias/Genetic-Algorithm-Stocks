from random import choice, random
from copy import deepcopy

from fitness import check_fitness
from chromosome import make_chromosome
from population import get_buy_short, get_high_low


def elitist(population: list, x: int):
    assert x != 0, "x cannot be 0."
    population.sort(key=lambda member: check_fitness(member))
    return population[-x:]


def tournament(population: list, x: int):
    assert x != 0, "x cannot be 0."
    winners = list()
    for _ in range(0, x):
        contestant1 = choice(population)
        contestant2 = choice(population)
        if check_fitness(contestant1) > check_fitness(contestant2):
            winners.append(contestant1)
        else:
            winners.append(contestant2)
    return winners


def selection(do_elitist: bool, population: list, x: int):
    if do_elitist:
        return elitist(population, x)
    else:
        return tournament(population, x)


def uniform(chromosome1: list, chromosome2: list):
    new_chromosome = list()
    for i in range(0, len(chromosome1)):
        new_chromosome.append(choice([chromosome1[i], chromosome2[i]]))
    return make_chromosome(*new_chromosome)


def k_point(chromosome1: list, chromosome2: list):
    return make_chromosome(*chromosome1[:2], *chromosome2[2:])


def crossover(do_uniform: bool, breeding_pool: list, pop_size: int):
    new_population = deepcopy(breeding_pool)
    for _ in range(0, pop_size-len(breeding_pool)):
        father = choice(breeding_pool)
        mother = choice(breeding_pool)
        if do_uniform:
            crossover_func = uniform
        else:
            crossover_func = k_point
        new_population.append(crossover_func(father, mother))
    return new_population


def mutation(population: list, chance_of_mutation: float):
    for i in range(0, len(population)):
        for j in range(0, len(population[0])):
            r = random()
            if r >= chance_of_mutation:
                if j == 4:
                    population[i] = make_chromosome(*population[i][:j], get_buy_short())
                else:
                    population[i] = make_chromosome(*population[i][:j], get_high_low(), *population[i][j+1:])
    return population

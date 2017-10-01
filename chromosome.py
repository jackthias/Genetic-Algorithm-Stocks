import numbers


def make_chromosome(day_1_low, day_1_high, day_2_low, day_2_high, buy_or_short):
    assert isinstance(day_1_low, numbers.Number), "day_1_low, {}, is not a number.".format(day_1_low)
    assert isinstance(day_2_low, numbers.Number), "day_2_low, {}, is not a number.".format(day_2_low)
    assert isinstance(day_1_high, numbers.Number), "day_1_high, {}, is not a number.".format(day_1_high)
    assert isinstance(day_2_high, numbers.Number), "day_2_high, {}, is not a number.".format(day_2_high)
    assert (isinstance(buy_or_short, int) and (buy_or_short == 0 or buy_or_short == 1)) \
        or isinstance(buy_or_short, bool), "buy_or_short is not bool or int"

    if day_1_low > day_1_high:
        day_1_low, day_1_high = day_1_high, day_1_high

    if day_2_low > day_2_high:
        day_2_low, day_2_high = day_2_high, day_2_low

    assert day_1_low <= day_1_high, "day_1_low is not the smaller number. ({}, {})".format(day_1_low, day_1_high)
    assert day_2_low <= day_2_low, "day_2_low is not the smaller number. ({}, {})".format(day_2_low, day_2_high)
    return [day_1_low, day_1_high, day_2_low, day_2_high, bool(buy_or_short)]


def fits_chromosome(file, chromosome):
    assert isinstance(file, list) and len(file) == 3, "file isn't in the right format: {}" % file
    assert isinstance(chromosome, list) \
        and len(chromosome) == 5, "chromosome isn't in the right format: {}" % chromosome

    i = 0
    for day in file[:-1]:
        if not chromosome[i] <= day <= chromosome[i + 1]:
            return False
        i += 2
    return True

test = False
if test:
    file_test = [-0.12, -0.81, -6.80]
    chromosome_test = make_chromosome(0, -5, 0.9, -3.1, 1)
    print(fits_chromosome(file_test, chromosome_test))

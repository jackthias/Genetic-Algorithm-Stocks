from chromosome import fits_chromosome, make_chromosome

files = []
# files.append("genAlgData1.txt")
# files.append("genAlgData2.txt")
files.append("handmadeTest1.txt")
non_match_penalty = -5000


def get_all_data():
    formatted_data = list()
    for file_name in files:
        file_stream = open(file_name, 'r')
        raw_data = file_stream.readlines()
        for line in raw_data:
            data_points = line[:-1].split('\t')
            for i in range(0, len(data_points)):
                data_points[i] = float(data_points[i])
            formatted_data.append(data_points)
    return formatted_data


def check_entry(entry, chromosome_to_inspect, match):
    if fits_chromosome(entry, chromosome_to_inspect):
        match[0] = True
        if chromosome_to_inspect[-1] == 0:
            return entry[-1] * -1
        else:
            return entry[-1]
    else:
        return 0


def check_fitness(chromosome_to_inspect):
    fitness = 0
    data = get_all_data()
    match = [False]
    for entry in data:
        fitness += check_entry(entry, chromosome_to_inspect, match)
    if not match[0]:
        return non_match_penalty
    return fitness

print(check_fitness(make_chromosome(-500000000, -50000001, -0.9, 3.1, 1)))

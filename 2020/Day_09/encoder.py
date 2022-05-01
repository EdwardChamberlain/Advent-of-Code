import itertools


def validate_value(preamble, value):
    results = [(x + y) for x, y in itertools.combinations(preamble, 2)]
    return value in results

def validate_list(data, preamble):
    for i, d in enumerate(data[preamble:]):
        truthy = validate_value(data[i:i+preamble], d)

        if not truthy:
            return d

def find_range(data, search_value):
    for n in range(len(data)):
        accumulator = 0
        for p, i in enumerate(data[n:]):
            accumulator += i

            if accumulator == search_value:
                data_range = data[n:n+p+1]
                if not len(data_range) == 0:
                    return data_range

            if accumulator > search_value:
                continue
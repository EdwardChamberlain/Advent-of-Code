import functools


def calc_delta(cur, pre):
    return cur - pre

def valid_delta(delta):
    return 0 < delta <=3

def forward_connections(value, data):
    res = []
    for i in data:
        if valid_delta(calc_delta(i, value)):
            res.append(i)
    return res

def all_forward_connections(data):
    return {i:forward_connections(i, data) for i in data}

def calcualte_possible_permutations(start, dict_data, end):
    @functools.lru_cache()
    def rec_get_paths2(start):
        if start == end:
            return 1

        downstream = sum([rec_get_paths2(i) for i in dict_data[start]])
        return downstream

    return rec_get_paths2(start)

import sys
import os
import itertools


def get_data():
    with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
        data = f.read()
        data = data.split('\n')
        data = list(map(int, data))
    return data


def move_list_value(move_index, data):
    value = data.pop(move_index)
    end_index = (move_index + value[1]) % len(data)
    if end_index == 0:
        end_index = len(data) + 1
    data.insert(end_index, value)


def mix_list(data, mixes=1):
    mutable_data = data.copy()
    for _ in range(mixes):
        for d in data:
            index = mutable_data.index(d)
            move_list_value(index, mutable_data)
    return mutable_data


def get_index_values(data, indexes):
    zero_index = data.index([i for i in data if i[1] == 0][0])
    values = []
    for n in indexes:
        index = (n + zero_index) % len(data)
        values.append(data[index][1])
    return values


def pt_1(data):
    data = list(enumerate(data))
    mixed_data = mix_list(data)

    numbers_to_sum = [1000, 2000, 3000]
    total = get_index_values(mixed_data, numbers_to_sum)

    print(sum(total))


def pt_2(data):
    decryption_key = 811589153
    data = list(map(lambda x: x * decryption_key, data))
    data = list(enumerate(data))
    mixed_data = mix_list(data, mixes=10)

    numbers_to_sum = [1000, 2000, 3000]
    total = get_index_values(mixed_data, numbers_to_sum)

    print(sum(total))


if __name__ == '__main__':
    data = get_data()

    pt_1(data)
    pt_2(data)
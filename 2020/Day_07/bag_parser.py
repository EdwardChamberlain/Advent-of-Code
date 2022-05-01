import re

RESULT = []

def get_bag_name(input_string):
    bags = re.search(r'(\w+ \w+) bags', input_string)
    return bags[1]

def get_bag_contents(input_string):
    bags = re.findall(r'(\w+) (\w+ \w+) bag', input_string)

    bags_ins = []
    for i in bags:
        try:
            bags_ins.append((int(i[0]), i[1]))
        except ValueError:
            bags_ins = [None]

    return bags_ins

def build_bags_dict(data):
    bags_dict = {}
    for i in data:
        bag_name = get_bag_name(i)
        bag_contents = get_bag_contents(i)

        bags_dict[bag_name] = bag_contents

    return bags_dict

def rec_containing_bags2(bags_dict, search_term):
    result = []

    for k, v in bags_dict.items():
        if search_term in [i[1] for i in v if i is not None]:
            result.append(k)
            next_level = rec_containing_bags(bags_dict, k)
            result.append(*next_level)

    return result

def rec_containing_bags(bag_dict, search_term, reset=True):
    global RESULT
    if reset:
        RESULT = []

    for k, v in bag_dict.items():
        if search_term in [i[1] for i in v if i is not None]:
            RESULT.append(k)
            rec_containing_bags(bag_dict, k, reset=False)
    return RESULT

def total_containing_bags(bags_list):
    try:
        total = [i[0] for i in bags_list]
    except TypeError:
        return 0
    return sum(total)

def rec_total_bags_inside(bags_dict, bag_type):
    bags_inside = total_containing_bags(bags_dict[bag_type])
    
    for i in bags_dict[bag_type]:
        if i is not None:
            bags_inside += rec_total_bags_inside(bags_dict, i[1]) * i[0]

    return bags_inside
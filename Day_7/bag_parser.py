import re

RESULT = []

def get_bag_name(input_string):
    bags = re.search('(\w+ \w+) bags', input_string)
    return bags[1]

def get_bag_contents(input_string):
    bags = re.findall('(\w+) (\w+ \w+) bag', input_string)

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

def get_containing_bags(bag_dict, search_term, reset=True):
    global RESULT
    if reset:
        RESULT = []

    for k, v in bag_dict.items():
        if search_term in [i[1] for i in v if i is not None]:
            RESULT.append(k)
            print(f"{search_term} is in {k}")
            get_containing_bags(bag_dict, k, reset=False)
    return RESULT

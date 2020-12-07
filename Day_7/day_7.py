import bag_parser
import collections

with open("Day_7/input_7.txt", 'r') as f:
    data = f.readlines()

bags_dict = bag_parser.build_bags_dict(data)

result = bag_parser.get_containing_bags(bags_dict, 'shiny gold')
print(len(collections.Counter(result).keys()))


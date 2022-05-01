import bag_parser
import collections
MY_BAG = 'shiny gold'

with open("2020/Day_07/input_7.txt", 'r') as f:
    data = f.readlines()

bags_dict = bag_parser.build_bags_dict(data)

bagsklfdhjg = bag_parser.rec_containing_bags2(bags_dict, MY_BAG)
print(len(collections.Counter(bagsklfdhjg).keys()))

result = bag_parser.rec_containing_bags(bags_dict, MY_BAG)
print(f"Total Bags that could contain a {MY_BAG} bag: {len(collections.Counter(result).keys())}")

bags_inside = bag_parser.rec_total_bags_inside(bags_dict, MY_BAG)
print(f"Bags inside my {MY_BAG}: {bags_inside}")
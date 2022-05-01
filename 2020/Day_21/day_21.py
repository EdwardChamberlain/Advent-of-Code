from gc import collect
import re
import collections


with open("2020/Day_21/input_21.txt", 'r') as f:
    data = [i.strip() for i in f.readlines()]


food = []
for i in data:
    x = {
        'ing': i.split('(')[0].strip().split(' '),
        'all': i.split('(')[1].strip(')').replace('contains ', '').split(' '),
    }
    x['all'] = [i.strip(',') for i in x['all']]
    food.append(x)

allergen_count = collections.Counter()
ing_count = collections.Counter()
allergens = []
ingredients = []
for f in food: 
    for ing in f['ing']:
        ing_count[ing] += 1
        ingredients.append(ing)
        for ale in f['all']:
            allergen_count[(ing, ale)] += 1
            allergens.append(ale)

allergens = set(allergens)
ingredients_set = set(ingredients)

confirmed_allergen = []
for i in ingredients_set:
    for a in allergens:
        if ing_count[i] == allergen_count[(i, a)]:
            print(i, a)
            confirmed_allergen.append(i)
   
result = set(ingredients) - set(confirmed_allergen)

for i in result:

    print(f"{i:>10}: {ingredients.count(i)}")
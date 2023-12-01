import sys
import os


nums = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}


def convert_strings_to_numbers(x: str, pt_2=True):
    result = []

    # get actual numbers
    for i, v in enumerate(x):
        if v.isnumeric():
            result.append((i, v))

    # Get stupid text numbers
    if pt_2:
        for k, v in nums.items():
            indexes = [i for i in range(len(x)) if x.startswith(k, i)]
            for i in indexes:
                result.append((i, v))

    # Condense to an actual string
    result = [
        i[1]
        for i in sorted(result, key=lambda x: x[0])
    ]
    result = ''.join(result)
    return result    


with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()
data = data.split('\n')

results = []
for d in data:
    d = convert_strings_to_numbers(d)

    value = int(d[0] + d[-1])
    results.append(value)

print(sum(results))


# def convert_strings_to_numbers_regex(x: str):
#     regex_result = re.findall(r'one|two|three|four|five|six|seven|eight|nine|zero|0|1|2|3|4|5|6|7|8|9', d, overlapped=True)
#     result_regex = [
#         nums[i] if i in nums else i
#         for i in regex_result
#     ]
#     result_regex = ''.join(result_regex)
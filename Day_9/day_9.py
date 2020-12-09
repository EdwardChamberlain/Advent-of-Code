import encoder


PREAMBLE = 25

with open("Day_9/input_9.txt", 'r') as f:
    data = f.readlines()
data = [int(i) for i in data]

invalid_value = encoder.validate_list(data, PREAMBLE)
print(f"Invalid Value = {invalid_value}")


data_range = encoder.find_range(data, invalid_value)
result = min(data_range) + max(data_range)
print(f"Pt 2 Result: {result}")
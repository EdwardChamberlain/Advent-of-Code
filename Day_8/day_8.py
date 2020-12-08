import instruction_parser

with open("Day_8/input_8.txt", 'r') as f:
    data = f.readlines()

instructions = instruction_parser.parse_lines(data)


exit_code, acc = instruction_parser.execute_boot(instructions)
print(f"Accumulator after one loop: {acc}")


for n, i in enumerate(instructions):
    ins = instructions.copy()
    ins[n] = instruction_parser.mutate_data(i)

    exit_code, acc = instruction_parser.execute_boot(ins)

    if exit_code == 0:
        print(f"Accumulator in fixed program: {acc}")
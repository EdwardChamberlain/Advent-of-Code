def parse_line(line):
    line = line.split()
    line[1] = int(line[1])
    return line

def parse_lines(data):
    lines = [parse_line(i) for i in data]
    return lines

def execute_command(command):
    if command[0] == 'nop':
        return 1, 0
    elif command[0] == 'acc':
        return 1, command[1]
    elif command[0] == 'jmp':
        return command[1], 0
    else:
        raise NotImplementedError

def execute_boot(instructions):
    PROG_COUNTER = 0
    PROG_DONE = []
    ACCUMULATOR  = 0
    try:
        while True:
            if PROG_COUNTER in PROG_DONE:
                return 1, ACCUMULATOR
            PROG_DONE.append(PROG_COUNTER)

            dprog, dacc = execute_command(instructions[PROG_COUNTER])
            PROG_COUNTER += dprog
            ACCUMULATOR += dacc

    except IndexError:
        return 0, ACCUMULATOR

def mutate_data(line):
    line = list(line)
    if line[0] == 'nop':
        line[0] = 'jmp'
    elif line[0] == 'jmp':
        line[0] = 'nop'
    return line
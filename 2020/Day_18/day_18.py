import homework_solver


with open("2020/Day_18/input_18.txt", 'r') as f:
    data = [i.strip() for i in f.readlines()]

result = [homework_solver.solve(i) for i in data]
print(f"Pt 1: {sum(result)}")

result = [homework_solver.solve2(i) for i in data]
print(f"Pt 2: {sum(result)}")
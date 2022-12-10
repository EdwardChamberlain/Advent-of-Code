import sys
import os


def sum_folder(path: str) -> int:
    counter = 0
    for i in os.listdir(path):
        file = path + '/' + i

        if os.path.isdir(file):
            counter += sum_folder(file)
        else:
            with open(file, 'r') as file:
                size = int(file.read())
            counter += size

    return counter


def get_all_dirs(path):
    dirs_total = []
    for root, dirs, _ in os.walk(path):
        dirs = [root + '/' + d for d in dirs]
        dirs_total += dirs
    return dirs_total


def generate_files(root_path):
    path = []
    for cmd in data:
        if cmd == 'cd /':
            path = root_path

        elif cmd == 'cd ..':
            path = path.rsplit('/', maxsplit=1)[0]

        elif cmd.startswith('cd'):
            new_path = cmd.split(' ')[-1]
            path += '/' + new_path

        elif cmd.startswith('ls'):
            files = cmd.split('\n')[1:]
            files = [
                f if f.startswith('dir ') else f.split(' ')
                for f in files
            ]

            for f in files:
                if isinstance(f, str):
                    os.mkdir(path + '/' + f.split(' ')[-1])
                    continue

                with open(path + '/' + f[1], 'w') as file:
                    file.write(f[0])


def get_current_space(root_path, storage_size):
    return STORAGE_SIZE - sum_folder(root_path)


with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()
    data = data.split('$ ')[1:]
    data = [d.strip() for d in data]

root_path = '2022/Day_07/sys'

# Generate File Structure
generate_files(root_path)

# Pt 1
dirs = get_all_dirs(root_path)
dir_sizes = [sum_folder(d) for d in dirs]
dirs_under_100000 = [d for d in dir_sizes if d <= 100000]

print(sum(dirs_under_100000))

# Pt 2
STORAGE_SIZE = 70000000
REQUIRED_SIZE = 30000000

current_space = get_current_space(root_path, STORAGE_SIZE)
space_to_free = REQUIRED_SIZE - current_space

dirs_that_would_free_enough_space = [d for d in dir_sizes if d > space_to_free]
print(min(dirs_that_would_free_enough_space))

class Board:
    def __init__(self, board_string: str):
        board_string = b.split('\n')
        width = 3
        self.board = [
            [
                int(row[i:i+width].strip())
                for i in range(0, len(row), width)
            ]
            for row in board_string
        ]

    def __repr__(self):
        return  "----------\n" + "\n".join(
            [
                str(i)
                for i in self.board
            ]
        ) + "\n----------"

    def is_win(self) -> bool:
        if self.check_rows() or self.check_cols():
            return True
        else:
            return False

    def check_rows(self) -> bool:
        for r in self.board:
            if r.count('*') == len(r):
                return True
        return False

    def check_cols(self) -> bool:
        rotated_board = [
            [
                i[n]
                for i in self.board
            ]
            for n in range(len(self.board[0]))
        ]

        for r in rotated_board:
            if r.count('*') == len(r):
                return True
        return False

    def check_number(self, value: int):
        for y, r in enumerate(self.board):
            for x, v in enumerate(r):
                if v == value:
                    self.board[y][x] = '*'

    def sum_board(self) -> int:
        # for r in self.board:
        #     print(r)
        #     r = [i for i in r if i != '*']
        #     print(r)
        # exit()

        result = sum([
            sum([i for i in r if i != '*'])
            for r in self.board
        ])
        return result



with open('inputs/day_4.txt') as f:
    data = f.read()
    data = data.split('\n\n')

call_numbers = data[0].split(',')
call_numbers = [int(i) for i in call_numbers]

boards_raw = data[1:]

boards = []
for b in boards_raw:
    boards.append(Board(b))


# for i in call_numbers:
#     for n, b in enumerate(boards):
#         b.check_number(i)

#         if b.is_win():
#             print("WINNER", n)
#             print(b.sum_board() * i)
#             break
#     else:
#         continue
#     break

winning_boards = []
final_board = False
for i in call_numbers:
    for n, b in enumerate(boards):
        if n in winning_boards:
            continue

        b.check_number(i)

        if b.is_win():
            if final_board:
                print("WINNER", n)
                print(b.sum_board() * i)
                exit()
            else:
                winning_boards.append(n)        
        else:
            if len(winning_boards) == len(boards) - 1:
                final_board = True

print(winning_boards)
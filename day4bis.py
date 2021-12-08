class BingoBoard:
    def __init__(self, lines):
        self.board = [[False for n in range(5)] for y in range(5)]
        self.num_to_position = { 
                n: (x, y) 
                for y, line in enumerate(lines) 
                for x, n in enumerate([int(c) for c in line.strip().split(' ') if c != ''])
            }

        print(self.board)
        print(self.num_to_position)

    def call(self, n):
        pos = self.num_to_position.get(n)
        if pos:
            self.board[pos[0]][pos[1]] = True
        else:
            return None

        if any([self.check_col(c) for c in range(5)] + [self.check_row(r) for r in range(5)]):
            print(self.board)
            return sum([n for n, (x, y) in self.num_to_position.items() if not self.board[x][y]]) * n
        else:
            return None

    def check_col(self, n):
        return sum([self.board[n][y] for y in range(5)]) == 5

    def check_row(self, n):
        return sum([self.board[x][n] for x in range(5)]) == 5

with open('day4in', 'r') as f:
    lines = f.readlines()

# first one called numbers
cn = [int(n) for n in lines.pop(0).strip().split(',')]

def gen_boards(lines):
    while lines:
        while lines[0].strip() == '':
            lines = lines[1:]
        yield BingoBoard(lines[0:5])
        lines = lines[5:]

boards = list(gen_boards(lines))

for n in cn:
    calls = [(b.call(n), b) for b in boards]
    boards = [b for (call, b) in calls if call is None]
    just_called = [call for (call, b) in calls if call is not None]

    if not boards:
        print(just_called)
        break


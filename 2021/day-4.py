import time


class Bingo:
    def __init__(self, grid):
        self.grid = list(map(lambda l: list(map(int, l.split())), grid))
        self.marks = [[False for _ in range(len(self.grid[r]))]
                      for r in range(len(self.grid))]

        self.lookup = {}
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                self.lookup[self.grid[r][c]] = (r, c)

    def mark(self, n):
        pos = self.lookup.get(n, None)
        if pos is not None:
            self.marks[pos[0]][pos[1]] = True

    def check_win(self):
        # check horizontal
        for r in range(len(self.marks)):
            if all(self.marks[r]):
                return True
        # check vertical
        for c in range(len(self.marks[0])):
            if all(self.marks[i][c] for i in range(len(self.marks))):
                return True
        return False

    def score(self):
        # True and N returns N
        # False and N returns 0
        # We want all the False ones, so invert the boolean
        return sum(not self.marks[r][c] and self.grid[r][c]
                   for r in range(len(self.marks))
                   for c in range(len(self.marks[r])))

    def print(self):
        width = len(str(max(max(self.grid, key=max))))
        for row in self.grid:
            print(' '.join(map(lambda n: f"{n:{width}}", row)))


def main():
    p1_score, p2_score = None, None

    with open('2021/input/4.txt', 'r') as f:
        lines = list(map(lambda l: l.strip(), f.readlines()))
    numbers, board_defs = lines[0], lines[2:]

    numbers = list(map(int, numbers.split(',')))

    boards = [Bingo(board_defs[(i*5)+i:(i*5)+i+5])
              for i in range(board_defs.count('')+1)]

    wins = [False] * len(boards)
    for n in numbers:
        for i, b in enumerate(boards):
            b.mark(n)

            last_win = wins[i]
            wins[i] = b.check_win()

            # If we haven't had a p1_score before, this is the first win
            if p1_score == None and wins[i]:
                p1_score = n * b.score()

            # If all are marked now but weren't before this board,
            # then this is the final winner
            elif not last_win and all(wins):
                p2_score = n * b.score()
                break

        if p2_score:
            break

    return p1_score, p2_score


if __name__ == '__main__':
    t1 = time.time()
    p1_score, p2_score = main()
    t2 = time.time()

    print(f"P1: {p1_score}")  # => 38913
    print(f"P2: {p2_score}")  # => 16836

    print(f"Took {t2 - t1}s")

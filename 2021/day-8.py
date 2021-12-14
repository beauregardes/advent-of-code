import time


def main():
    with open('2021/input/8.txt', 'r') as f:
        lines = list(map(lambda l: l.strip(), f.readlines()))

    p1_ans = 0

    for l in lines:
        signals, output = l.split(' | ')
        outputs = output.split()

        p1_ans += sum(len(o) in [2, 3, 4, 7] for o in outputs)

    return p1_ans, 0


if __name__ == '__main__':
    t1 = time.time()
    p1_ans, p2_ans = main()
    t2 = time.time()

    print(f"P1: {p1_ans}")  # => 369
    print(f"P2: {p2_ans}")  # =>

    print(f"Took {t2 - t1}s")

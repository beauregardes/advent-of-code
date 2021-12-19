import time


def main():
    with open('2021/input/14.txt', 'r') as f:
        lines = list(map(lambda l: l.strip(), f.readlines()))
    template = lines[0]
    rules = dict(map(lambda l: l.split(' -> '), lines[2:]))

    polymer = {}
    for i in range(len(template) - 1):
        pair = template[i:i+2]
        polymer[pair] = polymer.get(pair, 0) + 1

    letter_counts = {}
    for c in template:
        letter_counts[c] = letter_counts.get(c, 0) + 1

    for i in range(40):
        polymer_changes = {}

        for p, a in rules.items():
            p_count = polymer.get(p, 0)
            if p_count > 0:
                polymer_changes[p] = polymer_changes.get(p, 0) - p_count

                p1, p2 = p[0] + a, a + p[1]
                polymer_changes[p1] = polymer_changes.get(p1, 0) + p_count
                polymer_changes[p2] = polymer_changes.get(p2, 0) + p_count

                letter_counts[a] = letter_counts.get(a, 0) + p_count

        for p, c in polymer_changes.items():
            polymer[p] = polymer.get(p, 0) + c

        if i == 9:
            min_letter_count = min(letter_counts.items(), key=lambda e: e[1])
            max_letter_count = max(letter_counts.items(), key=lambda e: e[1])
            p1_ans = max_letter_count[1] - min_letter_count[1]

    max_letter_count = max(letter_counts.items(), key=lambda e: e[1])
    min_letter_count = min(letter_counts.items(), key=lambda e: e[1])
    p2_ans = max_letter_count[1] - min_letter_count[1]

    return p1_ans, p2_ans


if __name__ == '__main__':
    t1 = time.time()
    p1_ans, p2_ans = main()
    t2 = time.time()

    print(f"P1: {p1_ans}")  # => 4517
    print(f"P2: {p2_ans}")  # => 4704817645083

    print(f"Took {t2 - t1}s")

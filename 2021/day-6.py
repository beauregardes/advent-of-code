import time


def main():
    with open('2021/input/6.txt', 'r') as f:
        initial_fish_timers = list(map(int, f.read().strip().split(',')))

    fish_phase_counts = [0] * 9
    for t in initial_fish_timers:
        fish_phase_counts[t] += 1

    p1_ans = 0

    for i in range(1, 257):
        reset_count = fish_phase_counts[0]  # How many fish will be born

        # Shift all the fish counts down
        for t in range(len(fish_phase_counts) - 1):
            fish_phase_counts[t] = fish_phase_counts[t + 1]

        fish_phase_counts[6] += reset_count  # Reset the fish that gave birth
        fish_phase_counts[8] = reset_count  # Set the number of brand new fish

        if i == 80:
            p1_ans = sum(fish_phase_counts)

    return p1_ans, sum(fish_phase_counts)


if __name__ == '__main__':
    t1 = time.time()
    p1_ans, p2_ans = main()
    t2 = time.time()

    print(f"P1: {p1_ans}")  # => 365862
    print(f"P2: {p2_ans}")  # => 1653250886439
    print(f"Took {t2 - t1}s") 
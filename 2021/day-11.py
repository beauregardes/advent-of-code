import numpy as np
import time


def main():
    with open('2021/input/11.txt', 'r') as f:
        energy_levels = np.array(list(map(lambda l: list(map(int, list(l.strip()))), f.readlines())))

    p1_ans, p2_ans = 0, 0

    i = 1
    while True:
        # increment all the levels
        energy_levels += 1

        flashed = np.zeros(energy_levels.shape)
        while (energy_levels > 9).any():
            locs = np.transpose(np.nonzero(energy_levels > 9))
            all_flashed = True
            for l in locs:
                if not flashed[l[0], l[1]]:
                    sr = 0 if l[0]-1 < 0 else l[0]-1
                    er = l[0]+2
                    sc = 0 if l[1]-1 < 0 else l[1]-1
                    ec = l[1]+2
                    energy_levels[sr:er,sc:ec] += 1
                    flashed[l[0], l[1]] = 1
                    all_flashed = False

                    # Increment i, but not if we're past the first 100 steps
                    if i < 100:
                        p1_ans += 1
            if all_flashed:
                break
        locs = np.transpose(np.nonzero(energy_levels > 9))
        energy_levels[locs[:,0], locs[:,1]] = 0
        
        if (energy_levels == 0).all():
            p2_ans = i
            break
    
        i += 1

    return p1_ans, p2_ans


if __name__ == '__main__':
    t1 = time.time()
    p1_ans, p2_ans = main()
    t2 = time.time()

    print(f"P1: {p1_ans}")  # => 1683
    print(f"P2: {p2_ans}")  # => 788

    print(f"Took {t2 - t1}s")

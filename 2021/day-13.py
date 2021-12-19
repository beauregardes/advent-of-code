import time

import numpy as np


def p_paper(paper):
    for y in range(paper.shape[0]):
        for x in range(paper.shape[1]):
            print('#' if paper[y][x] > 0 else ' ', end='')
        print()


def main():
    with open('2021/input/13.txt', 'r') as f:
        lines = list(map(lambda l: l.strip(), f.readlines()))
    points = lines[0:lines.index('')]
    folds = lines[lines.index('')+1:]

    points = np.array(list(map(lambda p: list(map(int, p.split(','))), points)))

    folds = list(map(lambda f: f[len('fold along '):].split('='), folds))   
    folds = list(map(lambda f: [f[0], int(f[1])], folds))

    max_x = np.max(points[:,0])
    max_y = np.max(points[:,1])

    paper = np.zeros((max_y+1, max_x+1))
    paper[points[:,1], points[:,0]] = 1

    # Assumption being made here that the portion you're folding up/left
    # would not be larger than the piece you're folding it onto. This held
    # true for the input given, but this would break if that wasn't the case
    for i, f in enumerate(folds):
        if f[0] == 'y':
            # Right down the middle
            if f[1] == (paper.shape[0] - 1) / 2:
                fold_portion = np.flip(paper[f[1]+1:,:], 0)
                paper = paper[:f[1],:] + fold_portion
            # To the bottom
            else:
                fold_portion = np.flip(paper[f[1]+1:,:], 0)
                offset = f[1] - ((paper.shape[0] // 2) - 1)
                paper[offset:f[1],:] += fold_portion
                paper = np.delete(paper, np.arange(f[1], paper.shape[0]), 0)

        else:
            # Right down the middle
            if (paper.shape[1] - 1) / 2 == f[1]:
                fold_portion = np.flip(paper[:,f[1]+1:], 1)
                paper = paper[:,:f[1]] + fold_portion
            # To the right
            else:
                fold_portion = np.flip(paper[:,f[1]+1:], 1)
                offset = f[1] - ((paper.shape[1] // 2) - 1)
                paper[:,offset:f[1]] += fold_portion
                paper = np.delete(paper, np.arange(f[1], paper.shape[1]), 1)
        
        if i == 0:
            p1_ans = np.sum(paper > 0)

    # Print the p2 answer
    p_paper(paper)

    return p1_ans, "Read the letters that were printed, I ain't parsing that out"


if __name__ == '__main__':
    t1 = time.time()
    p1_ans, p2_ans = main()
    t2 = time.time()

    print(f"P1: {p1_ans}")  # => 618
    print(f"P2: {p2_ans}")  # => ALREKFKU

    print(f"Took {t2 - t1}s")

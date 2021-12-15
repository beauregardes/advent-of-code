from collections import deque
import time


def main():
    open_pair = {')': '(', ']': '[', '}': '{', '>': '<'}
    error_score = {')': 3, ']': 57, '}': 1197, '>': 25137}
    complete_score = {'(': 1, '[': 2, '{': 3, '<': 4}

    with open('2021/input/10.txt', 'r') as f:
        lines = list(map(lambda l: l.strip(), f.readlines()))

    p1_ans = 0
    p2_scores = []

    open_stack = deque()
    for l in lines:
      open_stack.clear()
      corrupted = False

      counts = {'(': 0, '[': 0, '{': 0, '<': 0}
      for c in l:
        if c in counts.keys():
          open_stack.append(c)
        elif c in open_pair.keys():
          if open_stack[-1] != open_pair[c]:
            p1_ans += error_score[c]
            corrupted = True
            break
          else:
            open_stack.pop()

      if not corrupted and len(open_stack) > 0:
        p2_scores.append(0)
        while len(open_stack) > 0:
          c = open_stack.pop()
          p2_scores[-1] *= 5
          p2_scores[-1] += complete_score[c]

    return p1_ans, sorted(p2_scores)[len(p2_scores) // 2]

if __name__ == '__main__':
    t1 = time.time()
    p1_ans, p2_ans = main()
    t2 = time.time()

    print(f"P1: {p1_ans}")  # => 469755
    print(f"P2: {p2_ans}")  # => 2762335572

    print(f"Took {t2 - t1}s")

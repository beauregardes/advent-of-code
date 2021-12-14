def calc(measurements, window_size):
  ans = 0
  for i in range(len(measurements) - window_size):
    w1 = measurements[i:i+window_size]
    w2 = measurements[i+1:i+1+window_size]
    if sum(map(int, w1)) < sum(map(int, w2)):
      ans += 1
  return ans


def main():
  with open('2021/input/1.txt', 'r') as f:
    measurements = f.readlines()

  p1_ans = calc(measurements, 1)
  p2_ans = calc(measurements, 3)

  return p1_ans, p2_ans


if __name__ == '__main__':
  p1_ans, p2_ans = main()

  print(f"P1: {p1_ans}")
  print(f"P2: {p2_ans}")

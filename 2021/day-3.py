def calc_power_consumption(readings):
  reading_bit_count = len(readings[0].strip())
  readings = [int(r, base=2) for r in readings]

  gamma_rate = ''
  epsilon_rate = ''
  for i in range(reading_bit_count - 1, -1, -1):
    count_1s = sum(r >= 2**i for r in readings)

    if count_1s > len(readings) // 2:
      gamma_rate += '1'
      epsilon_rate += '0'
    else:
      gamma_rate += '0'
      epsilon_rate += '1'
    
    readings = [r - 2**i if r >= 2**i else r for r in readings]

  return int(gamma_rate, 2) * int(epsilon_rate, 2)

def calc_life_support_rating(readings):
  reading_bit_count = len(readings[0].strip())
  readings = [int(r, base=2) for r in readings]

  oxygen_generator_readings = readings.copy()
  for i in range(reading_bit_count - 1, -1, -1):
    count_1s = sum(((r >> i) & 1) == 1 for r in oxygen_generator_readings)
    if count_1s >= len(oxygen_generator_readings) / 2:
      oxygen_generator_readings = list(filter(lambda r: ((r >> i) & 1) == 1, oxygen_generator_readings))
    else:
      oxygen_generator_readings = list(filter(lambda r: ((r >> i) & 1) == 0, oxygen_generator_readings))
    if len(oxygen_generator_readings) == 1:
      break

  co2_scrubber_readings = readings.copy()
  for i in range(reading_bit_count - 1, -1, -1):
    count_1s = sum(((r >> i) & 1) == 1 for r in co2_scrubber_readings)
    if count_1s < len(co2_scrubber_readings) / 2:
      co2_scrubber_readings = list(filter(lambda r: ((r >> i) & 1) == 1, co2_scrubber_readings))
    else:
      co2_scrubber_readings = list(filter(lambda r: ((r >> i) & 1) == 0, co2_scrubber_readings))
    if len(co2_scrubber_readings) == 1:
      break

  return oxygen_generator_readings[0] * co2_scrubber_readings[0]

def main():
  with open('2021/input/3.txt', 'r') as f:
    readings = f.readlines()

  power_consumption = calc_power_consumption(readings)
  life_support_rating = calc_life_support_rating(readings)

  return power_consumption, life_support_rating

if __name__ == '__main__':
  p1_ans, p2_ans = main()

  print(f"P1: {p1_ans}")
  print(f"P2: {p2_ans}")

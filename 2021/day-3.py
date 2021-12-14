import time


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
    def chkbit(r, i, v):
        return ((r >> i) & 1) == v

    reading_bit_count = len(readings[0].strip())
    readings = [int(r, base=2) for r in readings]

    ox_rdngs = readings.copy()
    for i in range(reading_bit_count - 1, -1, -1):
        count_1s = sum(chkbit(r, i, 1) for r in ox_rdngs)
        if count_1s >= len(ox_rdngs) / 2:
            ox_rdngs = list(filter(lambda r: chkbit(r, i, 1), ox_rdngs))
        else:
            ox_rdngs = list(filter(lambda r: chkbit(r, i, 0), ox_rdngs))
        if len(ox_rdngs) == 1:
            break

    co2_rdngs = readings.copy()
    for i in range(reading_bit_count - 1, -1, -1):
        count_1s = sum(chkbit(r, i, 1) for r in co2_rdngs)
        if count_1s < len(co2_rdngs) / 2:
            co2_rdngs = list(filter(lambda r: chkbit(r, i, 1), co2_rdngs))
        else:
            co2_rdngs = list(filter(lambda r: chkbit(r, i, 0), co2_rdngs))
        if len(co2_rdngs) == 1:
            break

    return ox_rdngs[0] * co2_rdngs[0]


def main():
    with open('2021/input/3.txt', 'r') as f:
        readings = f.readlines()

    power_consumption = calc_power_consumption(readings)
    life_support_rating = calc_life_support_rating(readings)

    return power_consumption, life_support_rating


if __name__ == '__main__':
    t1 = time.time()
    p1_ans, p2_ans = main()
    t2 = time.time()

    print(f"P1: {p1_ans}")  # => 1092896
    print(f"P2: {p2_ans}")  # => 4672151

    print(f"Took {t2 - t1}s")

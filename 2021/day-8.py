import time

#
#   00000
#  5     1
#  5     1
#   66666
#  4     2
#  4     2
#   33333
#

def decode_number(encoded_num):
    n = ''.join(map(str, encoded_num))
    if   n == '012345':  return '0'
    elif n == '12':      return '1'
    elif n == '01346':   return '2'
    elif n == '01236':   return '3'
    elif n == '1256':    return '4'
    elif n == '02356':   return '5'
    elif n == '023456':  return '6'
    elif n == '012':     return '7'
    elif n == '0123456': return '8'
    elif n == '012356':  return '9'
    else:
        print(f"Invalid number: {n}")
        return '0'

def decode_signals(signals, outputs):
    options = [set(), set(), set(), set(), set(), set(), set()]

    one = next(filter(lambda s: len(s) == 2, signals))
    # Slots 1 and 2 could be either component of 1
    options[1].update(one)
    options[2].update(one)

    seven = next(filter(lambda s: len(s) == 3, signals))
    seven_minus_one = seven.difference(one)
    # Slot 0 must be the single different element from 7
    options[0].add(list(seven_minus_one)[0])  

    four = next(filter(lambda s: len(s) == 4, signals))
    four_minus_one = four.difference(one)
    # Slots 5 and 6 are the difference between 4 and 1
    options[5].update(four_minus_one)
    options[6].update(four_minus_one)

    eight = next(filter(lambda s: len(s) == 7, signals))
    eight_minus_four_and_0 = eight.difference(four)
    eight_minus_four_and_0 = eight_minus_four_and_0.difference(options[0])
    # Slots 3 and 4 are the difference between 8 and 4 + the 0 slot
    options[3].update(eight_minus_four_and_0)
    options[4].update(eight_minus_four_and_0)

    # 0 will be the slot with only one of the components of 5/6 w all others
    lst5 = list(options[5])
    zero_base = set().union(options[0], options[1], options[3])
    zero_opt_1 = zero_base.union({lst5[0]})
    zero_opt_2 = zero_base.union({lst5[1]})
    zero = next(filter(lambda s: s in [zero_opt_1, zero_opt_2], signals))
    # Now we know slots 5 and 6, remove the extra options
    options[6] = options[6].difference(zero)
    options[5] = options[5].difference(options[6])

    # 5 will be one of four options:
    # 1) 0, 5, 6, 2[0], 3[0]
    # 2) 0, 5, 6, 2[0], 3[1]
    # 3) 0, 5, 6, 2[1], 3[0]
    # 4) 0, 5, 6, 2[1], 3[1]
    lst2 = list(options[2])
    lst3 = list(options[3])
    five_base = set().union(options[0], options[5], options[6])
    five_opt_1 = five_base.union({lst2[0], lst3[0]})
    five_opt_2 = five_base.union({lst2[0], lst3[1]})
    five_opt_3 = five_base.union({lst2[1], lst3[0]})
    five_opt_4 = five_base.union({lst2[1], lst3[1]})
    five = next(filter(lambda s: s in [five_opt_1, five_opt_2, five_opt_3, five_opt_4], signals))
    # Now we can get all options down to a single element
    options[1] = options[1].difference(five)
    options[2] = options[2].difference(options[1])
    options[4] = options[4].difference(five)
    options[3] = options[3].difference(options[4])

    # The index of the single element in each option corresponds to the
    # digit we'll use to encode that signal to a number
    mappings = {}
    for i, o in enumerate(options):
        mappings[list(o)[0]] = i
    
    # Now use that mapping to get the individual digits of our number as
    # an encoded string of which part of the display is set, and combine them
    num = ''
    for o in outputs:
        encoded_num = sorted(map(lambda n: mappings[n], o))
        num += decode_number(encoded_num)

    return int(num)


def main():
    with open('2021/input/8.txt', 'r') as f:
        lines = list(map(lambda l: l.strip(), f.readlines()))

    p1_ans, p2_ans = 0, 0

    for l in lines:
        signals, output = l.split(' | ')
        signals = list(map(set, signals.split()))
        outputs = list(map(sorted, output.split()))

        p1_ans += sum(len(o) in [2, 3, 4, 7] for o in outputs)
        p2_ans += decode_signals(signals, outputs)

    return p1_ans, p2_ans


if __name__ == '__main__':
    t1 = time.time()
    p1_ans, p2_ans = main()
    t2 = time.time()

    print(f"P1: {p1_ans}")  # => 369
    print(f"P2: {p2_ans}")  # => 1031553

    print(f"Took {t2 - t1}s")

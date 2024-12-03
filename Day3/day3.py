"""AoC2024 Day3"""

import re


def main():
    """Lets do som regexp"""
    with open('./AoC2024/Day3/input.txt', encoding="utf-8") as f:
        puzzle_input = f.readlines()
        
        # Part 1
        reg = re.compile('mul\(\d{1,3},\d{1,3}\)')
        numbers = re.compile('\d{1,3}')
        sum = 0
        for l in puzzle_input:
            matching = reg.findall(l)
            for m in matching:
                n = numbers.findall(m)
                sum += int(n[0]) * int(n[1])
        print(sum)


if __name__ == '__main__':
    main()
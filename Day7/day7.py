"""AoC 2024 Day4"""
from collections import deque
from typing import List

def check_test_value(value:int, numbers:List[int])->bool:
    """Reverse check if numbers add/multiply to value"""

    if len(numbers) == 1:
        return value == numbers[0]

    last_n = numbers[-1]

    if (value / last_n).is_integer():
        if check_test_value(value/last_n, numbers[:-1]):
            return True

    return check_test_value(value-last_n, numbers[:-1])

def main():
    """Lets look for the correct calibrations""" 
    with open('./AoC2024/Day7/input.txt', encoding="utf-8") as f:
        puzzle = {}
        for x in f.readlines():
            value, numbers = x.strip().split(':')
            puzzle[int(value)] = list(map(int,numbers.split()))

        sum_values = [k for k,v in puzzle.items() if check_test_value(k,v)]
        print(sum(sum_values))

if __name__ == '__main__':
    main()

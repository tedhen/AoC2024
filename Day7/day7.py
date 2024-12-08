"""AoC 2024 Day4"""
from typing import List

def check_with_concat(value:int, numbers:List[int])->bool:
    """Reverse check if numbers add, multiply or concat to value"""

    if len(numbers) <= 1:
        return value == numbers[0]

    last_n = numbers[-1]

    if (value / last_n).is_integer():
        if check_with_concat(value/last_n, numbers[:-1]):
            return True

    if last_n < value:
        if check_with_concat(value-last_n, numbers[:-1]):
            return True

        if str(int(value)).endswith(str(last_n)) :
            next_possible_value = int(str(int(value))[:-(len(str(last_n)))])
            if check_with_concat(next_possible_value, numbers[:-1]):
                return True

    return False

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
        puzzle = []
        for x in f.readlines():
            value, numbers = x.strip().split(':')
            puzzle.append((int(value),[map(int,numbers.split())]))


        # Part 1
        sum_values = [k for (k,v) in puzzle if check_test_value(k,v)]
        print(f"Part:1 {sum(sum_values)}")

        # Part 2
        sum_values = [k for (k,v) in puzzle if check_with_concat(k,v)]
        print(f"Part:2 {sum(sum_values)}")

if __name__ == '__main__':
    main()

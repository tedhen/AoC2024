"""AoC2024 Day11"""
from collections import Counter

def blink(puzzle):
    """Run the blink loop"""
    new_puzzle = Counter()
    for k,v in puzzle.items():
        k_str = str(k)
        k_l = len(k_str)
        if k == 0:
            new_puzzle[1] += v
        elif k_l % 2 == 0:
            f_h=k_str[:int(k_l/2)]
            s_h=k_str[int(k_l/2):]
            new_puzzle[int(f_h)] += v
            new_puzzle[int(s_h)] += v
        else:
            new_k = k * 2024
            new_puzzle[new_k] += v
    return new_puzzle

def main():
    """Dont blink to much""" 
    with open('./Day11/input.txt', encoding="utf-8") as f:
        puzzle = Counter([int(x) for x in f.readline().strip().split()])


        # Part 1, bink 25 times
        for _ in range(25):
            puzzle = blink(puzzle)

        print(sum(puzzle.values()))

        # Part 2, blink 75 times. (50 More)
        for _ in range(50):
            puzzle = blink(puzzle)
        print(sum(puzzle.values()))

if __name__ == '__main__':
    main()

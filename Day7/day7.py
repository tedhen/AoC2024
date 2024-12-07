"""AoC 2024 Day4"""
from collections import deque

def main():
    """Lets look for the correct calibrations""" 
    with open('./Day7/test.txt', encoding="utf-8") as f:
        puzzle = {}
        for x in f.readlines():
            value, numbers = x.strip().split(':')
            puzzle[int(value)] = list(map(int,numbers.split()))


if __name__ == '__main__':
    main()

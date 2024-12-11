from collections import Counter

def main():
    """Lets look for the correct calibrations""" 
    with open('./Day11/test.txt', encoding="utf-8") as f:
        puzzle = Counter([x for x in f.readline().strip().split()])

        print(puzzle)

if __name__ == '__main__':
    main()

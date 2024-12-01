"""AoC 2024 Day 1"""

def main():
    """It is simple today, do everting in one function"""
    with open('./AoC2024/Day1/input.txt', encoding="utf-8") as f:
        puzzle_input = f.readlines()
        a_list = list()
        b_list = list()
        for x in puzzle_input:
            a, b = x.split()
            a_list.append(int(a))
            b_list.append(int(b))
        a_list.sort()
        b_list.sort()
        distance = 0
        for a, b in zip(a_list,b_list):
            distance += abs(a-b)
        print(distance)

        appearance = dict()
        for x in b_list:
            if x in appearance:
                appearance[x] += 1
            else:
                appearance[x] = 1

        score = 0
        for x in a_list:
            if x in appearance:
                score += x * appearance[x]
        print(score)

if __name__ == '__main__':
    main()

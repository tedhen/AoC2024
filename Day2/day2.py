"""AoC 2024 Day 2"""

def safety_test(report):
    """Test if the levels are safe"""
    inc = True

    if report[0] > report[1]:
        inc = False

    for x, y in zip(report, report[1:]):
        if not 1 <= abs(x-y) <= 3:
            return False
        if x == y:
            return False

        if inc:
            if x > y:
                return False
        else:
            if x < y:
                return False
    return True

def extended_safety(report):
    """Test if removing any of the levels makes it safe"""
    if safety_test(report=report):
        return True

    for i in range(len(report)):
        new_report = report.copy()
        new_report.pop(i)
        if safety_test(new_report):
            return True

    return False

def main():
    """It is simple today, do everting in one function"""
    with open('./AoC2024/Day2/input.txt', encoding="utf-8") as f:
        puzzle_input = f.readlines()
        test = []
        ext_test = []
        for x in puzzle_input:
            report = [int(y) for y in x.split()]
            test.append(safety_test(report))
            ext_test.append(extended_safety(report))
        print(sum(test))
        print(sum(ext_test))

if __name__ == '__main__':
    main()

"""AoC2024 day10"""
from typing import Tuple, List

def is_valid_coord(y:int,x:int, y_size:int, x_size:int)->bool:
    """Check if a coord is inside a matrix"""
    return not ( x < 0 or y < 0 or x >= x_size or y >= y_size)

def coord_generator(y:int,x:int, y_size:int, x_size:int) -> List[Tuple[int,int]]:
    """Generate a list of all coords in horizontal, vertical and diagonal from location"""
    coords = []
    # Horizontal
    potential_cords =(y, x + 1)
    if is_valid_coord(*potential_cords, y_size, x_size):
        coords.append(potential_cords)
    potential_cords =(y, x - 1)
    if is_valid_coord(*potential_cords, y_size, x_size):
        coords.append(potential_cords)

    # Vertical
    potential_cords =(y+1, x)
    if is_valid_coord(*potential_cords, y_size, x_size):
        coords.append(potential_cords)
    potential_cords =(y-1, x)
    if is_valid_coord(*potential_cords, y_size, x_size):
        coords.append(potential_cords)

    return coords


def score_a_trail(y:int, x:int, hiking_map:List[List[int]])->int:
    """Given a position, search for a trail, if not possible return 0"""
    value = hiking_map[y][x]
    if value == 9:
        return [(y,x)]

    possible_paths = coord_generator(y, x, len(hiking_map), len(hiking_map[0]))
    score = []
    for p_y, p_x in possible_paths:
        if hiking_map[p_y][p_x] - value == 1:
            score.extend(score_a_trail(p_y, p_x, hiking_map))

    return score

def main():
    """Let's plan a hiking route""" 
    with open('./Day10/input.txt', encoding="utf-8") as f:
        puzzle = []
        for x in f.readlines():
            puzzle.append([int(y)for y in x.strip()])

        start_pos = []
        for i, x in enumerate(puzzle):
            for j, y in enumerate(x):
                if y == 0:
                    start_pos.append((i, j))

        trail_paths = [ score_a_trail(y, x, puzzle) for (y,x) in start_pos ]

        trail_score = [len(set(x)) for x in trail_paths] # aka uniqe trail ends
        print(f"Part:1 {sum(trail_score)}")

        # Part 2
        trail_summary = sum([len(x) for x in trail_paths])
        print(f"Part:1 {trail_summary}")

if __name__ == '__main__':
    main()

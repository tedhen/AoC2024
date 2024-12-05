"""AoC 2024 Day4"""
from typing import Tuple, List

def find_offsets(s:str, sub_s:str)->List[int]:
    """Find the start of all (possibly-overlapping) instances of a sub_string"""
    offs = -1
    while True:
        offs = s.find(sub_s, offs+1)
        if offs == -1:
            break
        else:
            yield offs

def is_valid_coord(y:int,x:int, y_size:int, x_size:int)->bool:
    """Check if a coord is inside a matrix"""
    return not ( x < 0 or y < 0 or x >= x_size or y >= y_size)

def coord_generator(y:int,x:int, y_size:int, x_size:int, step:int=1) -> List[List[Tuple[int,int]]]:
    """Generate a list of all coords in horizontal, vertical and diagonal from location"""
    coords = []
    # Horizontal
    potential_cords = [(y, x + offs) for offs in range(step)]
    if is_valid_coord(*potential_cords[-1], y_size, x_size):
        coords.append(potential_cords)
    potential_cords = [(y, x - offs) for offs in range(step)]
    if is_valid_coord(*potential_cords[-1], y_size, x_size):
        coords.append(potential_cords)
    # Vertical
    potential_cords = [(y+offs, x) for offs in range(step)]
    if is_valid_coord(*potential_cords[-1], y_size, x_size):
        coords.append(potential_cords)
    potential_cords = [(y-offs, x) for offs in range(step)]
    if is_valid_coord(*potential_cords[-1], y_size, x_size):
        coords.append(potential_cords)

    # Diagonal
    potential_cords = [(y + offs, x + offs) for offs in range(step)]
    if is_valid_coord(*potential_cords[-1], y_size, x_size):
        coords.append(potential_cords)
    potential_cords = [(y + offs, x - offs) for offs in range(step)]
    if is_valid_coord(*potential_cords[-1], y_size, x_size):
        coords.append(potential_cords)
    potential_cords = [(y - offs, x + offs) for offs in range(step)]
    if is_valid_coord(*potential_cords[-1], y_size, x_size):
        coords.append(potential_cords)
    potential_cords = [(y - offs, x - offs) for offs in range(step)]
    if is_valid_coord(*potential_cords[-1], y_size, x_size):
        coords.append(potential_cords)

    return coords

def get_coords_value(pos,matrix):
    values = []
    for (y,x) in pos:
        values.append(matrix[y][x])
    return values

def mas_generator(y,x, y_size, x_size):
    step = 3
    coords = []
    first_diagonal = [((y-1) + offs, (x-1) + offs) for offs in range(step)]
    if all([is_valid_coord(*pos, y_size, x_size) for pos in first_diagonal]):
        coords.append(first_diagonal)
    second_diagonal = [((y-1) + offs, (x+1) - offs) for offs in range(step)]
    if all([is_valid_coord(*pos, y_size, x_size) for pos in second_diagonal]):
        coords.append(second_diagonal)

    if len(coords) == 2:
        return coords

    return []

def check_for_xmas(coords:List[Tuple[int,int]], puzzle:List[str])->bool:
    """Could XMAS be at this locations? Lets find out"""
    xmas = 'XMAS'
    for i, (y,x) in enumerate(coords):
        if not puzzle[y][x] == xmas[i]:
            return False
    return True

def check_for_mas(coords:List[Tuple[int,int]], puzzle:List[str])->bool:
    """check for double mas"""
    if not coords:
        return False
    mases = [''.join(get_coords_value(diag, puzzle)) for diag in coords]
    m = [mas == 'MAS' or mas == 'SAM' for mas in mases]
    return all(m)

def main():
    """Lets hunt for XMAS""" 
    with open('./AoC2024/Day4/input.txt', encoding="utf-8") as f:
        puzzle = [x.strip() for x in f.readlines()]

        x_location = []
        for i, y in enumerate(puzzle):
            loc = [(i, j) for j in find_offsets(y, 'X')]
            x_location.extend(loc)

        potential_xmas_coords = []
        for coord in x_location:
            potential_xmas_coords.extend(coord_generator(*coord, y_size=len(puzzle), x_size=len(puzzle[0]), step=4))

        xmas = [check_for_xmas(coords, puzzle) for coords in potential_xmas_coords]
        print(sum(xmas))

        a_location = []
        for i, y in enumerate(puzzle):
            loc = [(i, j) for j in find_offsets(y, 'A')]
            a_location.extend(loc)

        potential_mas_coords = []
        for coord in a_location:
            potential_mas_coords.append(mas_generator(*coord, y_size=len(puzzle), x_size=len(puzzle[0])))

        mases = [check_for_mas(coords, puzzle) for coords in potential_mas_coords]
        print(sum(mases))

if __name__ == '__main__':
    main()

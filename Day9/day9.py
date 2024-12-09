"""AoC 2024 Day9"""
from collections import deque
from typing import List, Deque

def compact(harddrive:List, freelist:Deque):
    """Compact the harddrive"""
    for i,x in reversed(list(enumerate(harddrive))):
        if not freelist:
            return

        if  not x == "FREE":
            first_free = freelist.popleft()
            if first_free > i:
                # Can't compact more, free is after current data
                return
            harddrive[first_free] = harddrive[i]
            harddrive[i] = "FREE"


def swap_file(harddrive, from_pos, to_pos):
    """Swap file locations"""
    f_i, f_size = from_pos
    t_i, t_size = to_pos

    if f_size > t_size:
        raise ValueError("File size to big for new location")

    for i in range(f_size):
        harddrive[f_i + i], harddrive[t_i + i] = harddrive[t_i + i], harddrive[f_i + i]


def move_files(harddrive, file_catalog, freespace):
    """Try to move all files to the left"""
    for f in reversed(file_catalog):
        f_start, f_size = file_catalog[f]

        for i, (space_index, space_size) in enumerate(freespace):
            if space_index > f_start:
                # only move files to the left
                break

            if space_size >= f_size:
                swap_file(harddrive, (f_start, f_size), (space_index, space_size))
                if space_size - f_size > 0:
                    freespace[i] = (space_index + f_size, space_size-f_size)
                else:
                    freespace.pop(i)
                break


def generate_harddrive(puzzle):
    """Generate a harddvie layout from puzzle specification"""
    # every other item in the input is freespace information
    is_it_freespace = [False if i%2==0 else True for i in range(len(puzzle))]

    harddrive = []
    freespace = deque()
    freespace_contigous = []
    file_catalog = {}

    index = 0
    file_id = -1
    for (x, free) in zip(puzzle, is_it_freespace):
        if not free:
            file_id += 1
            file_catalog[file_id] = (index,x)
        else:
            freespace_contigous.append((index, x))

        for _ in range(x):
            if free:
                freespace.append(index)
                harddrive.append('FREE')
            else:
                harddrive.append(file_id)

            index += 1
    return (harddrive, freespace, file_catalog, freespace_contigous)

def main():
    """Lets look for the correct calibrations""" 
    with open('./Day9/input.txt', encoding="utf-8") as f:
        raw = f.readline().strip()
        puzzle = [int(x) for x in raw]

        # Part 1
        harddrive,freespace, file_catalog, freespace_contigous = generate_harddrive(puzzle)
        compact(harddrive=harddrive, freelist=freespace)

        checksum = [x*i if x != 'FREE' else 0 for i,x in enumerate(harddrive)]
        print(sum(checksum))

        # Part 2
        harddrive,freespace, file_catalog, freespace_contigous = generate_harddrive(puzzle)
        move_files(harddrive, file_catalog, freespace_contigous)
        checksum = [x*i if x != 'FREE' else 0 for i,x in enumerate(harddrive)]
        print(sum(checksum))

if __name__ == '__main__':
    main()

#!/usr/bin/env python3


def read_grid(fname):
    with open(fname) as f:
        return [[int(x) for x in l.split()] for l in f.readlines()]


def output_grid(fname, grid, start, goal, path):
    # Mark start and goal pts
    grid[start[0]][start[1]] = 'S'
    grid[goal[0]][goal[1]] = 'G'

    # Mark intermediate path pts with '*'
    for i, p in enumerate(path):
        if 0 < i < len(path) - 1:
            grid[p[0]][p[1]] = '*'

    # Write grid to file: add space between columns and newline between rows
    with open(fname, 'w') as f:
        f.write('\n'.join(' '.join([str(col) for col in row]) for row in grid))

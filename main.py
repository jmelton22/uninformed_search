#!/usr/bin/env python3

from queue import Queue
from node import Node
from grid import read_grid, output_grid


def main():
    grid = read_grid('grid.txt')
    start = [1, 1]
    end = [5, 6]

    # Print grid: add space between columns and newline between rows
    print('\n'.join(' '.join([str(col) for col in row]) for row in grid))


if __name__ == '__main__':
    main()

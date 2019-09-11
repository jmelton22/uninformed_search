#!/usr/bin/env python3

from itertools import zip_longest

from queue import Queue, LifoQueue
from node import Node
import grid as g


def uninformed_search(grid, start, goal, breadth=True):
    current = Node(start, '')
    visited = []

    if breadth:
        unexplored = Queue()
    else:
        unexplored = LifoQueue()

    search(grid, current, goal, unexplored, visited)

    return visited


def search(grid, node, goal, unexplored, visited):
    visited.append(node)

    if node.value == goal:
        return
    else:
        expand_node(grid, node, visited, unexplored)

        if unexplored.empty():
            return False
        else:
            search(grid, unexplored.get(), goal, unexplored, visited)


# TODO: Clean up logic for node in visited list or in queue
def expand_node(grid, node, visited, unexplored):

    def in_queue(loc, unexplored):
        for each in list(unexplored.queue):
            if loc == each.value:
                return True
        return False

    def in_visited(loc, visited):
        for each in visited:
            if loc == each.value:
                return True
        return False

    for n in node.get_neighbors(grid):
        if not in_visited(n, visited) and not in_queue(n, unexplored):
            unexplored.put(Node(n, node))


def main():
    grid = g.read_grid('grid.txt')
    start = [1, 1]
    end = [5, 6]

    breadth_path = uninformed_search(grid, start, end)
    depth_path = uninformed_search(grid, start, end, breadth=False)

    print('Breadth   Depth')
    for b_node, d_node in zip_longest(breadth_path, depth_path):
        print(b_node.value, end=' \t ')
        if d_node:
            print(d_node.value)
        else:
            print(d_node)

    # g.output_grid(grid, start, end, path)

    # # Print grid: add space between columns and newline between rows
    # print('\n'.join(' '.join([str(col) for col in row]) for row in grid))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

from queue import Queue, LifoQueue
from node import Node
import grid as g


def uninformed_search(grid, start, goal, breadth=True):
    current = Node(start, '')
    visited, path = [], []
    unexplored = Queue() if breadth else LifoQueue()

    return search(grid, current, goal, unexplored, visited, path)


def search(grid, node, goal, unexplored, visited, path):
    visited.append(node)

    if node.value == goal:
        return set_path(node, path)
    else:
        expand_node(grid, node, visited, unexplored)

        if unexplored.empty():
            return None
        else:
            return search(grid, unexplored.get(), goal, unexplored, visited, path)


def set_path(node, path):
    path.append(node.value)
    if node.parent == '':
        return path
    else:
        return set_path(node.parent, path)


def expand_node(grid, node, visited, unexplored):
    def in_unexplored(loc, q):
        return True if loc in [each.value for each in list(q.queue)] else False

    def in_visited(loc, l):
        return True if loc in [each.value for each in l] else False

    for n in node.get_neighbors(grid):
        if not in_visited(n, visited) and not in_unexplored(n, unexplored):
            unexplored.put(Node(n, node))


def main():
    grid = g.read_grid('grid.txt')
    start = [1, 1]
    end = [5, 6]

    path = uninformed_search(grid, start, end)
    fname = 'breadth_path.txt'

    # path = uninformed_search(grid, start, end, breadth=False)
    # fname = 'depth_path.txt'

    if path is None:
        print('No path found.')
    else:
        g.output_grid(fname, grid, start, end, path)


if __name__ == '__main__':
    main()

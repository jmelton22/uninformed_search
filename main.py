#!/usr/bin/env python3

from queue import Queue, LifoQueue
from node import Node
import grid as g


def uninformed_search(grid, start, goal, breadth=True):
    current = Node(start, '')
    visited, path = [], []

    if breadth:
        unexplored = Queue()
    else:
        unexplored = LifoQueue()

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

    path = uninformed_search(grid, start, end)
    # path = uninformed_search(grid, start, end, breadth=False)

    if path is not None:
        g.output_grid('breadth_path.txt', grid, start, end, path)


if __name__ == '__main__':
    main()

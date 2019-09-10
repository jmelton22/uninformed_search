#!/usr/bin/env python3


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

    def get_neighbors(self, grid):
        up = [self.value[0] - 1, self.value[1]]
        right = [self.value[0], self.value[1] + 1]
        down = [self.value[0] + 1, self.value[1]]
        left = [self.value[0] - 1, self.value[1]]

        neighbors = []

        if grid[up[0]][up[1]] == 0:
            neighbors.append(up)
        if grid[right[0]][right[1]] == 0:
            neighbors.append(right)
        if grid[down[0]][down[1]] == 0:
            neighbors.append(down)
        if grid[left[0]][left[1]] == 0:
            neighbors.append(left)

        return neighbors

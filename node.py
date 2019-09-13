#!/usr/bin/env python3


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

    def get_neighbors(self, grid):
        up = [self.value[0] - 1, self.value[1]]
        right = [self.value[0], self.value[1] + 1]
        down = [self.value[0] + 1, self.value[1]]
        left = [self.value[0], self.value[1] - 1]

        return [coord for coord in [up, right, down, left] if grid[coord[0]][coord[1]] == 0]

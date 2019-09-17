#!/usr/bin/env python3


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

    def get_neighbors(self, grid):
        # First row nodes have no 'up' neighbor
        up = [self.value[0] - 1, self.value[1]] if self.value[0] > 0 else None
        # Last col nodes have no 'right' neighbor
        right = [self.value[0], self.value[1] + 1] if self.value[1] < len(grid[0]) - 1 else None
        # Last row nodes have no 'down' neighbor
        down = [self.value[0] + 1, self.value[1]] if self.value[0] < len(grid) - 1 else None
        # First col nodes have no 'left' neighbor
        left = [self.value[0], self.value[1] - 1] if self.value[1] > 0 else None

        # Return neighboring nodes which have value 0 in grid
        return [coord for coord in [up, right, down, left] if coord is not None and grid[coord[0]][coord[1]] == 0]

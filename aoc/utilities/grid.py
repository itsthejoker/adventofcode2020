class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.current_position = [0, 0]

    def slope(self, x, y):
        x, y = self.current_position
        line = self.grid[y]
        self.current_position[0] += x
        self.current_position[1] += y
        return line[14 % len(line)]

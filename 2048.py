"""
Clone of 2048 game.
"""
      
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    result1 = [0 for i in range(len(line))]
    i = 0
    j = 0
    while i < len(line):
        if line[i] != 0:
            result1[j] = line[i]
            j += 1
        i += 1
        
    result2 = [0 for i in range(len(line))]
    i = 0
    j = 0
    while i < len(line) - 1:
        if result1[i] == result1[i + 1]:
            result2[j] = result1[i] + result1[i + 1]
            i += 2
        else:
            result2[j] = result1[i]
            i += 1
        j += 1
    if i < len(result1):
        result2[j] = result1[i]
        i += 1
        j += 1
    return result2

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()
        self.init_tiles = {UP: [(0, i) for i in range(grid_width)],
                           DOWN: [(grid_height - 1, i) for i in range(grid_width)],
                           LEFT: [(i, 0) for i in range(grid_height)],
                           RIGHT: [(i, grid_width - 1) for i in range(grid_height)],
                           }
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self.grid = [[0 for i in range(self.grid_width)] for j in range(self.grid_height)]
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self.grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        origin_grid = []
        for lst in self.grid:
            origin_grid.append(lst[:])
        offset = OFFSETS[direction]
        for tile in self.init_tiles[direction]:
            indices = []
            lst = []
            row = tile[0]
            col = tile[1]
            while row >= 0 and row < self.grid_height and col >= 0 and col < self.grid_width:
                lst.append(self.grid[row][col])
                indices.append((row, col))
                row += offset[0]
                col += offset[1]
            lst = merge(lst)
            for i, index in enumerate(indices):
                self.grid[index[0]][index[1]] = lst[i]
        if self.grid != origin_grid:
            self.new_tile()
                           
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        row = random.randrange(self.grid_height)
        col = random.randrange(self.grid_width)
        while self.grid[row][col] != 0:
            row = random.randrange(self.grid_height)
            col = random.randrange(self.grid_width)
        time = random.random()
        if time > 0.9:
            self.grid[row][col] = 4
        else:
            self.grid[row][col] = 2
            
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        return self.grid[row][col]
if __name__ == "__main__":
    game = TwentyFortyEight(1, 1)
    game.new_tile()
    print game

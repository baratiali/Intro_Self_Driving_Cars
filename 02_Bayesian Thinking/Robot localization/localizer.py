#import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    norm_new_beliefs = []
    height = len(beliefs)
    width = len(beliefs[0])

    for j in range(height):
        r = []
        for i in range(width):
            belief = beliefs[j][i]
            if color == grid[j][i]:
                r.append(belief * p_hit)
            else:
                r.append(belief * p_miss)
        new_beliefs.append(r)

    Sum = 0
    for j in range(height):
        for i in range(width):
            Sum = Sum + new_beliefs[j][i]
    
    for j in range(0,height):
        r = []
        for i in range(0,width):
            r.append(new_beliefs[j][i]/Sum)
        norm_new_beliefs.append(r)
        
    return norm_new_beliefs


def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % height
            new_j = (j + dx ) % width
      
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)



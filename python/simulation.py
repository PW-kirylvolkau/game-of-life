import argparse
import numpy as np

################### ANOTHER APPROACH ######################

def runSimulation(grid,N = 20,steps = 5):
    for i in range(steps):
        new_grid = [len(grid[0])*[0] for i in range(len(grid))]
        # Update grid
        next_step(grid, new_grid)
        grid, new_grid = new_grid, grid

    return np.asarray(grid)


def next_step(grid, new_grid):
	for x in range(0, len(grid[0])):
		for y in range(0, len(grid)):
			live_neighbors = healthy_neighbors(x, y, grid)
			if grid[y][x]:
				if live_neighbors < 2 or live_neighbors > 3:
					new_grid[y][x] = 0
				else:
					new_grid[y][x] = grid[y][x]
			else:
				if live_neighbors == 3:
					new_grid[y][x] = 1


def healthy_neighbors(x, y, grid):
	live_neighbors = 0
	for i in range(-1, 2):
		testx = (x+i) % len(grid[0])
		for j in range(-1, 2):
			testy = (y+j) % len(grid)
			if j == 0 and i == 0:
				continue
			if grid[testy][testx] == 1:
				live_neighbors += 1
	return live_neighbors


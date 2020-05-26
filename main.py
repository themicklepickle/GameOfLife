# Project - Conway's Game of Life
# Main driver module
# Michael Xu
# May 19, 2020


# import all supporting modules
import pygame
import ast
from datetime import date, datetime
from functions import *
import sanitization as s

# display title screen
main_screen()

# input variables in terminal
print("INPUT PARAMETERS:")
grid_type = s.integer("Existing grid (0) or New grid (1): ", 0, 1)
if grid_type == 1:
	width = s.integer("Grid width: ", None, None)
	height = s.integer("Grid height: ", None, None)
gens = s.integer("Generations: ", 1, None)
mode = s.integer("Automatic (0) or Manual (1) Generations: ", 0, 1)
if mode == 0:
	delay = s.floating_point("Time Delay (secs): ", 0, None)
if grid_type == 1:
	print("DONE. Please return to game window")
	grid = input_grid(width, height)
else:
	grid = ast.literal_eval(input("Existing grid (one line matrix): "))
	print("DONE. Please return to game window.")

# write grid to history file for future reference
history = open("history.txt", "a")
history.write(f"date: {date.today().strftime('%m/%d/%y')}, time: {datetime.now().strftime('%H:%M:%S')}\n")
history.write("Copy: "+str(grid)+"\n")
history.write("[")
for row in range(len(grid)):
	if row == 0:
		history.write("[")
	else:
		history.write(" [")
	for col in range(len(grid[row])):
		if col == len(grid[row]) - 1:
			history.write(str(grid[row][col]))
		else:
			history.write(str(grid[row][col]) + ", ")
	if row == len(grid) - 1:
		history.write("]")
	else:
		history.write("],\n")
history.write("]\n\n")
history.close()

# main program
for generation in range(gens + 1):

	# draw grid in game window
	draw_grid(grid, generation, mode)

	# wait before proceeding to the next generation
	if mode == 0:
		pygame.time.delay(int(delay*1000))
		pygame.event.get()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			pygame.quit()
	else:
		while True:
			pygame.event.get()
			pygame.time.delay(100)
			keys = pygame.key.get_pressed()
			if keys[pygame.K_RETURN]:
				break
			if keys[pygame.K_ESCAPE]:
				pygame.quit()

	# update grid
	old_grid = grid.copy()
	for row in range(len(old_grid)):
		old_row = old_grid[row].copy()
		for col in range(len(old_row)):
			if alive(old_grid, (col, row)):
				old_row[col] = 1
			else:
				old_row[col] = 0
		grid[row] = old_row

# close pygame window
pygame.quit()

"""Advent of Code 2021 Day 02 - Dive"""

import numpy as np

instructions = np.loadtxt('input/day2.txt', dtype = [('direction', np.str_, 16), ('amount', int)])

x_position = 0
z_position = 0

#For each row in the list
for instruction in instructions:
    if instruction[0] == 'forward':
        x_position = x_position + instruction[1]
    elif instruction[0] == 'up':
        z_position = z_position - instruction[1]
    elif instruction[0] == 'down':
        z_position = z_position + instruction[1]

print("X Position: " + str(x_position))
print("Z Position: " + str(z_position))
print("Part 1 Answer: " + str(x_position*z_position))


## PART 2 ##
x_position = 0
z_position = 0
aim = 0

for instruction in instructions:
    if instruction[0] == 'forward':
        x_position = x_position + instruction[1]
        z_position = z_position + (aim*instruction[1])
    elif instruction[0] == 'up':
        aim = aim - instruction[1]
    elif instruction[0] == 'down':
        aim = aim + instruction[1] 

print("X Position: " + str(x_position))
print("Z Position: " + str(z_position))
print("Part 2 Answer: " + str(x_position*z_position))
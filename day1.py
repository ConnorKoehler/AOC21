"""Advent of Code 2021 Day 01 - Sonar Sweep"""

with open('input/day1.txt', 'r') as readings:
    depths = [int(number.strip()) for number in readings.readlines()]

increased = sum([1 for i in range(1, len(depths)) if depths[i] > depths[i-1]])

# Part one
print("Part 1 increases:", increased)

increased = sum([1 for i in range(3, len(depths)) if depths[i] > depths[i-3]])

# Part two
print("Part 2 increases:", increased)
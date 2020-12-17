#!/usr/bin/env python3

from collections import defaultdict
from copy import deepcopy
from rich.progress import track


def next3(dimension, origin, size):
  def neighbor_count(x, y, z):
      size = len(dimension)
      return [dimension[z + zi][y + yi][x + xi]
              for xi in range(-1, 2)
              for yi in range(-1, 2)
              for zi in range(-1, 2)
              if not (xi == yi and yi == zi and zi == 0) and
              all(0 <= s < size for s in [x + xi, y + yi, z + zi])
              ].count('#')

  new_dim = deepcopy(dimension)
  for z in range(origin, origin + size):
    for y in range(origin, origin + size):
      for x in range(origin, origin + size):
        count = neighbor_count(x, y, z)
        cell = dimension[z][y][x]
        if cell == '#' and not (2 <= count <= 3):
          new_dim[z][y][x] = '.'
        elif cell == '.' and count == 3:
          new_dim[z][y][x] = '#'

  return new_dim


def next4(dimension, origin, size):
  def neighbor_count(x, y, z, w):
      size = len(dimension)
      return [dimension[w + wi][z + zi][y + yi][x + xi]
              for xi in range(-1, 2)
              for yi in range(-1, 2)
              for zi in range(-1, 2)
              for wi in range(-1, 2)
              if not (xi == yi and yi == zi and zi == wi and wi == 0) and
              all(0 <= s < size for s in [x + xi, y + yi, z + zi, w + wi])
              ].count('#')

  new_dim = deepcopy(dimension)
  for w in range(origin, origin + size):
    for z in range(origin, origin + size):
      for y in range(origin, origin + size):
        for x in range(origin, origin + size):
          count = neighbor_count(x, y, z, w)
          cell = dimension[w][z][y][x]
          if cell == '#' and not (2 <= count <= 3):
            new_dim[w][z][y][x] = '.'
          elif cell == '.' and count == 3:
            new_dim[w][z][y][x] = '#'

  return new_dim


def solve_part1(dimension, origin, size, cycles=6):
  for _ in track(range(cycles), description="Cycles"):
    origin -= 1
    size += 2
    dimension = next3(dimension, origin, size)

  return sum(row.count('#')
             for plane in dimension
             for row in plane)


def solve_part2(dimension, origin, size, cycles=6):
  for _ in track(range(cycles), description="Cycles"):
    origin -= 1
    size += 2
    dimension = next4(dimension, origin, size)

  return sum(row.count('#')
             for instance in dimension
             for plane in instance
             for row in plane)


def read(file='input.txt', cycles=6):
  with open(file, 'r') as f:
    initial = [list(l) for l in f.read().splitlines()]
  size = len(initial) + 2 * cycles
  dimension = [[[['.' for _ in range(size)]
                 for _ in range(size)]
                for _ in range(size)]
               for _ in range(size)]

  origin = size // 2 - len(initial) // 2
  for y, row in enumerate(initial):
    for x, cell in enumerate(row):
      if cell == '#':
        dimension[origin][origin][origin + y][origin + x] = cell
  return dimension, origin, len(initial)


def main():
  dimension, origin, size = read()
  print("Part 1:", solve_part1(dimension[origin], origin, size))
  print("Part 2:", solve_part2(dimension, origin, size))


if __name__ == "__main__":
  main()

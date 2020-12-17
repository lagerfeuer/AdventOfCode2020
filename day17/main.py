#!/usr/bin/env python3

from collections import defaultdict
from copy import deepcopy


def _next(dimension, size, wr=(-1,1)):
  def neighbor_count(x, y, z, w=0, wr=wr):
      size = len(dimension)
      return [dimension[(w + wi,z + zi,y + yi,x + xi)]
              for xi in range(-1, 2)
              for yi in range(-1, 2)
              for zi in range(-1, 2)
              for wi in range(wr[0], wr[1] + 1)
              if not (xi == yi and yi == zi and zi == wi and wi == 0)
              ].count('#')

  new_dim = deepcopy(dimension)
  for w in range(-size, size + 1):
    for z in range(-size, size + 1):
      for y in range(-size, size + 1):
        for x in range(-size, size + 1):
          count = neighbor_count(x, y, z, w)
          cell = dimension[(w,z,y,x)]
          if cell == '#' and not (2 <= count <= 3):
            new_dim[(w,z,y,x)] = '.'
          elif cell == '.' and count == 3:
            new_dim[(w,z,y,x)] = '#'

  return new_dim


def solve_part1(dimension, size, cycles=6):
  for _ in range(cycles):
    size += 2
    dimension = _next(dimension, size // 2, wr=(0,0))

  return list(dimension.values()).count('#')


def solve_part2(dimension, size, cycles=6):
  for _ in range(cycles):
    size += 2
    dimension = _next(dimension, size // 2)

  return list(dimension.values()).count('#')


def read(file='input.txt', cycles=6):
  with open(file, 'r') as f:
    initial = [list(l) for l in f.read().splitlines()]
  dimension = defaultdict(lambda: '.')

  half = len(initial) // 2
  for y, row in enumerate(initial):
    for x, cell in enumerate(row):
      if cell == '#':
        dimension[(0, 0, y - half, x - half)] = cell
  return dimension, len(initial)


def main():
  dimension, size = read()
  print("Part 1:", solve_part1(dimension, size))
  print("Part 2:", solve_part2(dimension, size))


if __name__ == "__main__":
  main()

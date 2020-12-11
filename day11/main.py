#!/usr/bin/env python3

from copy import deepcopy


def is_occupied(seat_map, y, x):
  if 0 <= y < len(seat_map) and 0 <= x < len(seat_map[0]):
    return seat_map[y][x] == '#'
  return False


def part1(seat_map, y, x):
  return [
      is_occupied(seat_map, yi, xi)
      for yi in range(y - 1, y + 2)
      for xi in range(x - 1, x + 2)
      if y != yi or x != xi
  ].count(True)


def part2(seat_map, y, x):
  directions = [(ud, lr)
                for ud in range(-1, +2)
                for lr in range(-1, +2)
                if ud != 0 or lr != 0]
  neighbors = []
  for (yd, xd) in directions:
    yi, xi = y + yd, x + xd
    while 0 <= yi < len(seat_map) and 0 <= xi < len(seat_map[yi]) and seat_map[yi][xi] == '.':
      yi += yd
      xi += xd
    neighbors.append(is_occupied(seat_map, yi, xi))
  return neighbors.count(True)


def advance(seat_map, limit, occupied):
  changes = []

  for y, row in enumerate(seat_map):
    for x, seat in enumerate(row):
      if seat == '.':
        continue
      occupied_neighbors = occupied(seat_map, y, x)
      if seat == 'L' and occupied_neighbors == 0:
        changes.append((y, x, '#'))
      if seat == '#' and occupied_neighbors >= limit:
        changes.append((y, x, 'L'))

  for (y, x, val) in changes:
    seat_map[y][x] = val

  return len(changes)


def solve(seat_map, limit, func):
  while advance(seat_map, limit=limit, occupied=func):
    pass
  return sum(row.count('#') for row in seat_map)


def read(file='input.txt'):
  with open(file, 'r') as f:
    return [list(l) for l in f.read().strip().splitlines()]


def main():
  seat_map = read()
  print("Part 1:", solve(deepcopy(seat_map), limit=4, func=part1))
  print("Part 2:", solve(deepcopy(seat_map), limit=5, func=part2))


if __name__ == "__main__":
  main()

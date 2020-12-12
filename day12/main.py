#!/usr/bin/env python3

# Autocomplete worked (dec 11 22:42)

from collections import defaultdict
from itertools import groupby

CDIRS = 'N E S W'.split()


def d2c(degrees):
  """Convert degrees to cardinal direction."""
  ix = round(degrees / (360. / len(CDIRS)))
  return CDIRS[ix % len(CDIRS)]


def rotate(waypoint, deg, cw):
  """
  Rotate a waypoint, e.g. ((N, 10), (E, 5)) to ((S,5), (E, 10)).
  This keeps the N/S coordinates at the first position.
  """
  def _idx(i):
    tmp = clicks if cw else -clicks
    return (CDIRS.index(i) + tmp) % len(CDIRS)

  clicks = int(deg / 90)
  ((y, dy), (x, dx)) = waypoint
  new_y, new_x = CDIRS[_idx(y)], CDIRS[_idx(x)]
  y_pair = (new_y, dy)
  x_pair = (new_x, dx)
  # keep N/S as first pair
  return (y_pair, x_pair) if new_y in 'N S'.split() else (x_pair, y_pair)


def add(pos, move):
  """
  Add two matching or opposite cardinal directions.
  Final cardinal direction is correctly calculated, e.g. (N, 10) + (S, 20) = (S, 10).
  """
  (c, d), (c_add, d_add) = pos, move
  if c == c_add:
    return (c, d + d_add)
  else:
    d_new = d - d_add
    return (c if d_new >= 0 else c_add, abs(d_new))


def solve_part1(instructions):
  facing = 90  # east
  moves = defaultdict(int)
  for (direction, distance) in instructions:
    if direction == 'R':
      facing += distance
    elif direction == 'L':
      facing -= distance
    elif direction == 'F':
      moves[d2c(facing)] += distance
    else:
      moves[direction] += distance
  return abs(moves['N'] - moves['S']) + abs(moves['E'] - moves['W'])


def solve_part2(instructions, initial_waypoint=(('N', 1), ('E', 10))):
  waypoint = initial_waypoint
  moves = defaultdict(int)

  for instr in instructions:
    (op, arg) = instr
    ((cy, dy), (cx, dx)) = waypoint

    if op == 'F':
      for (c, dd) in waypoint:
        moves[c] += dd * arg
    elif op in 'N S'.split():
      waypoint = (add(waypoint[0], instr), (cx, dx))
    elif op in 'E W'.split():
      waypoint = ((cy, dy), add(waypoint[1], instr))
    else:
      waypoint = rotate(waypoint, arg, op == 'R')

  return abs(moves['N'] - moves['S']) + abs(moves['E'] - moves['W'])


def read(file='input.txt'):
  with open(file, 'r') as f:
    return [(l[0], int(l[1:])) for l in f.read().splitlines()]


def main():
  instructions = read()
  print("Part 1:", solve_part1(instructions))
  print("Part 2:", solve_part2(instructions))


if __name__ == "__main__":
  main()

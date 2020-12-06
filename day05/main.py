#!/usr/bin/env python3

"""
row and col are binary numbers. (row * 8 + col) is essentially (row << 3 | col),
meaning they are already binary encoded.
Simply replace FL and BR with 0 and 1 and parse the whole number.
"""
table = str.maketrans("FBLR", "0101")


def get_id(seat):
  return int(seat.translate(table), 2)


def solve_part1(ids):
  return max(ids)


def solve_part2(ids):
  for (a, b) in zip(ids, ids[1:]):
    if b - a == 2:
      return a + 1


def read(file='input.txt'):
  with open(file, 'r') as f:
    seats = sorted([s.strip() for s in f.readlines()])
  return list(map(get_id, seats))


def main():
  ids = read()
  print("Part 1:", solve_part1(ids))
  print("Part 2:", solve_part2(ids))


if __name__ == "__main__":
  main()

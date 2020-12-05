#!/usr/bin/env python3


def get_id(seat):
  row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
  col = int(seat[7:].replace('L', '0').replace('R', '1'), 2)
  return row * 8 + col


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

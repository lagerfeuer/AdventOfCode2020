#!/usr/bin/env python3

from functools import reduce


def solve(groups, func):
  return sum([len(reduce(func, g)) for g in groups])


def read(file='input.txt'):
  with open(file, 'r') as f:
    groups = [[set(s) for s in l.split('\n')]
              for l in f.read().strip().split('\n\n')]
  return groups


def main():
  groups = read()
  print("Part 1:", solve(groups, lambda a, b: a | b))
  print("Part 2:", solve(groups, lambda a, b: a & b))


if __name__ == "__main__":
  main()

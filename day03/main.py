#!/usr/bin/env python3

from functools import reduce


def get_tree(tree_map, y, x):
  tree_line = tree_map[y]
  return tree_line[x % len(tree_line)]


def solve_part1(tree_map, model=(3, 1)):
  cnt = 0
  x = y = 0
  while y < len(tree_map):
    if get_tree(tree_map, y, x) == '#':
      cnt += 1
    x += model[0]
    y += model[1]
  return cnt


def solve_part2(tree_map):
  models = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
  trees_encountered = [solve_part1(tree_map, model) for model in models]
  return reduce(lambda a, b: a * b, trees_encountered)


def read(file='input.txt'):
  with open(file, 'r') as f:
    lines = [l.strip() for l in f.readlines()]
  return lines


def main():
  tree_map = read()
  print("Part 1:", solve_part1(tree_map))
  print("Part 2:", solve_part2(tree_map))


if __name__ == "__main__":
  main()

#!/usr/bin/env python3

import sys
import re
from collections import defaultdict
from functools import lru_cache


def solve_part1(lookup_tbl, q='shiny gold'):
  seen = {q}
  queue = [q]
  while queue:
    bag = queue.pop(0)
    outer = lookup_tbl[bag]
    queue += list(outer)
    seen.update(outer)
  return len(seen) - 1


def solve_part2(rules, q='shiny gold'):
  @lru_cache(maxsize=256)
  def get_count(bag):
    contains = rules[bag]
    if contains is None:
      return 0

    tmp = sum(entry[1] * (1 + get_count(entry[0]))
              for entry in contains.items())
    return tmp

  return get_count(q)


def read(file='input.txt'):
  rules = {}
  lookup_tbl = defaultdict(set)
  with open(file, 'r') as f:
    lines = [re.sub(' bags?', '', l)
             .replace(' contain ', ':')
             .replace('no other', '')
             .replace(', ', ',')[:-1]
             for l in f.read().splitlines()]

  for line in lines:
    (outer, inners) = line.split(':')
    if not inners:
      rules[outer] = None
      continue
    inners = inners.split(',')

    tmp = {}
    for inner in inners:
      idx = inner.index(' ')
      (num, name) = int(inner[:idx]), inner[idx + 1:]
      tmp[name] = num
      lookup_tbl[name].add(outer)
    rules[outer] = tmp

  return (rules, lookup_tbl)


def main():
  (rules, lookup_tbl) = read()
  print("Part 1:", solve_part1(lookup_tbl))
  print("Part 2:", solve_part2(rules))


if __name__ == "__main__":
  main()

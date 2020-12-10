#!/usr/bin/env python3

from collections import Counter
from functools import cache


def solve_part1(adapters):
  chain = sorted(adapters + [0])
  chain.append(chain[-1] + 3)
  freq = Counter([b - a for (a, b) in zip(chain, chain[1:])])
  return freq[1] * freq[3]


def solve_part2(adapters):
  chain = sorted(adapters)
  chain.append(chain[-1] + 3)

  @cache
  def _get(n):
    if n == 0:
      return 1
    if n not in chain:
      return 0
    return _get(n-1) + _get(n-2) + _get(n-3)

  return _get(chain[-1])


def read(file='input.txt'):
  with open(file, 'r') as f:
    return [int(l) for l in f.read().splitlines()]


def main():
  adapters = read()
  print("Part 1:", solve_part1(adapters))
  print("Part 2:", solve_part2(adapters))


if __name__ == "__main__":
  main()

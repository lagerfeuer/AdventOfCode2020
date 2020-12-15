#!/usr/bin/env python3

from collections import defaultdict


def solve(starting_numbers, n=2020):
  numbers = defaultdict(list)
  for (i, e) in enumerate(starting_numbers):
    numbers[e].append(i)
  last = starting_numbers[-1]

  for i in range(len(numbers), n):
    if len(numbers[last]) > 1:
      last = i - (numbers[last][-2] + 1)
    else:
      last = 0
    numbers[last].append(i)

  return last



def read(file='input.txt'):
  with open(file, 'r') as f:
    return [int(x) for x in f.read().strip().split(',')]


def main():
  numbers = read()
  # numbers = read('test.txt')
  print("Part 1:", solve(numbers, n=2020))
  print("Part 2:", solve(numbers, n=30000000))


if __name__ == "__main__":
  main()

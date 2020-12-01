#!/usr/bin/env python3

def find_pair(lst, value=2020):
  h = {}
  for elem in lst:
    if other := h.get(elem, None):
      return (elem, other)
    h[value - elem] = elem
  return None


def find_triple(lst, value=2020):
  """
  Use two pointer technique
  """
  lst.sort()
  for x in range(len(lst) - 2):
    y = x + 1
    z = len(lst) - 1
    while y < z:
      tmp = lst[x] + lst[y] + lst[z]
      if tmp == value:
        return (lst[x], lst[y], lst[z])
      elif tmp < value:
        y += 1
      else:
        z -= 1
  return None


def solve_part1(numbers):
  pair = find_pair(numbers)
  return pair[0] * pair[1]

def solve_part2(numbers):
  pair = find_triple(numbers)
  return pair[0] * pair[1] * pair[2]

def main():
  with open('input.txt', 'r') as f:
    numbers = [int(x) for x in f.readlines()]

  print("Part 1:", solve_part1(numbers))
  print("Part 2:", solve_part2(numbers))


if __name__ == "__main__":
  main()

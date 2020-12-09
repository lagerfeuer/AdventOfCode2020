#!/usr/bin/env python3

from collections import deque


def find_pair(nums, value):
  h = {}
  for num in nums:
    inv = value - num
    if inv in h:
      return (h[inv], inv)
    h[num] = inv
  return None


def solve_part1(nums, preamble=25):
  window = deque(nums[:preamble])
  for num in nums[preamble:]:
    if not find_pair(list(window), num):
      return num
    window.popleft()
    window.append(num)


def solve_part2(nums, value):
  window = deque()
  for num in nums:
    while sum(window) > value:
      window.popleft()
    else:
      if sum(window) == value:
        break
      elif sum(window) < value:
        window.append(num)
  window = list(window)
  return min(window) + max(window)


def read(file='input.txt'):
  with open(file, 'r') as f:
    return [int(l) for l in f.read().splitlines()]


def main():
  nums = read()
  invalid_num = solve_part1(nums)
  print("Part 1:", invalid_num)
  print("Part 2:", solve_part2(nums, invalid_num))


if __name__ == "__main__":
  main()

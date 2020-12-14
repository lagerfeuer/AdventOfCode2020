#!/usr/bin/env python3
"""
Use Chinese Remainder Theorem with Extended Euclidean Algorithm, see:
https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
"""

from functools import reduce
from operator import mul


def crt(n, a):
  total = 0
  N = reduce(mul, n)
  for ni, ai in zip(n, a):
    p = N // ni
    total += ai * egcd(p, ni)[1] * p
  return total % N


def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		gcd, x, y = egcd(b % a, a)
		return (gcd, y - (b // a) * x, x)


def solve_part1(timestamp, shuttles):
  shuttle_times = [(sid, timestamp + (sid - (timestamp % sid)))
                   for sid in shuttles]
  sid, ts = min(shuttle_times, key=lambda e: e[1])
  return sid * (ts - timestamp)


def solve_part2(shuttles):
  ids = [(e - i, e) for i, e in enumerate(shuttles) if e != 'x']
  times, shuttles = [[a for a, b in ids],
                     [b for a, b in ids]]
  return crt(shuttles, times)


def read(file='input.txt'):
  with open(file, 'r') as f:
    timestamp = int(f.readline().strip())
    shuttles = [
        int(e) if e != 'x' else e for e in f.readline().strip().split(',')]
    return timestamp, shuttles


def main():
  timestamp, shuttles = read()
  print("Part 1:", solve_part1(
      timestamp, [sh for sh in shuttles if sh != 'x']))
  print("Part 2:", solve_part2(shuttles))


if __name__ == "__main__":
  main()

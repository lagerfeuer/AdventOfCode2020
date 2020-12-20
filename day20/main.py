#!/usr/bin/env python3

from collections import namedtuple, defaultdict
from functools import reduce
from operator import mul
from math import sqrt

ImageTile = namedtuple('ImageTile', 'data borders')


def get_borders(tile):
  borders = [  # CW borders
      tile[0],
      tile[-1],
      "".join([l[0] for l in tile]),
      "".join([l[-1] for l in tile]),
  ]
  return borders


def find_connected(data):
  connected = defaultdict(set)
  for tid1, t1 in data.items():
    for tid2, t2 in data.items():
      if tid1 == tid2:
        continue
      if any(t1b == t2b for t1b in t1.borders for t2b in t2.borders + [b[::-1] for b in t2.borders]):
        connected[tid1].add(tid2)
        connected[tid2].add(tid1)
        continue
  return connected

def construct_image(data):
  connected = find_connected(data)
  corners = [k for (k,v) in connected.items() if len(v) == 2]
  to_place = {data.keys()}
  n = int(sqrt(len(data)))
  result = [[-1 for _ in range(n)] for _ in range(n)]

  start = corners[0]
  tmp = connected[start]

def solve_part1(data):
  connected = find_connected(data)
  # corner tiles have only two connected ids
  return reduce(mul, [int(k) for (k, v) in connected.items() if len(v) == 2])


def solve_part2(data):
  image = construct_image(data)


def read(file='input.txt'):
  data = {}
  with open(file, 'r') as f:
    for block in f.read().split('\n\n'):
      lines = block.splitlines()
      id = lines[0][:-1].split()[1]
      tile = lines[1:]
      data[id] = ImageTile(tile, get_borders(tile))
  return data


def main():
  data = read()
  # data = read('test.txt')
  print("Part 1:", solve_part1(data))
  print("Part 2:", solve_part2(data))


if __name__ == "__main__":
  main()

#!/usr/bin/env python3

from collections import defaultdict
from itertools import permutations


def apply_mask(value: str, mask: str) -> str:
  """Takes two binary strings and returns a binary string."""
  result = [m if m != 'X' else v for (
      v, m) in zip(value.zfill(len(mask)), mask)]
  return "".join(result)


def resolve_address(addr: str, mask: str) -> str:
  """Takes two binary strings and returns a binary string."""
  def _combine(addr, mask, fluent):
    result = []
    fidx = 0
    for (bit, mbit) in zip(addr.zfill(len(mask)), mask):
      if mbit == 'X':
        result.append(fluent[fidx])
        fidx += 1
      elif mbit == '1':
        result.append(mbit)
      else:
        result.append(bit)
    return "".join(result)

  fluent_bits = mask.count('X')
  fluent_perms = [bin(x)[2:].zfill(fluent_bits)
                  for x in range(pow(2, fluent_bits))]
  addresses = [_combine(addr, mask, f) for f in fluent_perms]
  return addresses


def solve_part1(instructions):
  memory = defaultdict(int)
  mask = None
  for (op, arg) in instructions:
    if op == 'mask':
      mask = arg
    else:
      (loc, arg) = (arg[0], bin(int(arg[1]))[2:])
      memory[loc] = int(apply_mask(arg, mask), 2)
  return sum(memory.values())


def solve_part2(instructions):
  memory = defaultdict(int)
  mask = None
  for (op, arg) in instructions:
    if op == 'mask':
      mask = arg
    else:
      (loc, value) = (bin(int(arg[0]))[2:], int(arg[1]))
      for addr in resolve_address(loc, mask):
        memory[addr] = value
  return sum(memory.values())


def read(file='input.txt'):
  instructions = []
  with open(file, 'r') as f:
    for line in f.read().splitlines():
      (op, arg) = line.split(' = ')
      tmp = (op, arg)
      if op.startswith('mem'):
        location = op[4:-1]
        tmp = (op[:3], (int(location), arg))
      instructions.append(tmp)
  return instructions


def main():
  instructions = read()
  print("Part 1:", solve_part1(instructions))
  print("Part 2:", solve_part2(instructions))


if __name__ == "__main__":
  main()

#!/usr/bin/env python3

from enum import Enum


class Result(Enum):
  ENDLESS_LOOP = -1
  OK = 0
  CONTINUE = 1


class VM:
  def __init__(self, code):
    self.code = code
    self.ip = 0
    self.acc = 0
    self.visited = set()

  def run(self):
    result = None
    while (result := self.step()) == Result.CONTINUE:
      pass
    return result

  def step(self):
    if self.ip >= len(self.code):
      return Result.OK

    if self.ip in self.visited:
      return Result.ENDLESS_LOOP
    self.visited.add(self.ip)

    (op, arg) = self.code[self.ip]
    if op == 'acc':
      self.acc += arg
    elif op == 'jmp':
      self.ip += arg - 1
    else:
      pass
    self.ip += 1
    return Result.CONTINUE


def solve_part1(code):
  vm = VM(code)
  vm.run()
  return vm.acc


def solve_part2(code):
  """Brute Force"""
  def flip(instr):
    (op, arg) = instr
    return ('nop', arg) if op == 'jmp' else ('jmp', arg)

  nop_jmp = [i for i, (op, _) in enumerate(code) if op in 'nop jmp'.split()]
  while nop_jmp:
    idx = nop_jmp.pop()
    code[idx] = flip(code[idx])
    vm = VM(code)
    if vm.run() == Result.OK:
      return vm.acc
    code[idx] = flip(code[idx])


def read(file='input.txt'):
  with open(file, 'r') as f:
    code = [(op, int(arg))
            for l in f.read().splitlines()
            for (op, arg) in [l.split()]]
  return code


def main():
  code = read()
  print("Part 1:", solve_part1(code))
  print("Part 2:", solve_part2(code))


if __name__ == "__main__":
  main()

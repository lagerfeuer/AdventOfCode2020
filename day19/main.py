#!/usr/bin/env python3

from lark import Lark

import re


def solve(l, messages):
  def _parse(l, msg):
    try:
      l.parse(msg)
      return True
    except Exception as e:
      # print(e)
      return False

  return [_parse(l, msg) for msg in messages].count(True)


def read(file='input.txt', part2=False):
  with open(file, 'r') as f:
    (rules, messages) = f.read().split('\n\n')
  messages = [l.strip() for l in messages.splitlines()]

  if part2:
    rules = re.sub(r'8: 42', r'8: 42 | 42 8', rules)
    rules = re.sub(r'11: 42 31', r'11: 42 31 | 42 11 31', rules)

  grammar = re.sub(r'(\d+)', r'r\1', rules, flags=re.MULTILINE)
  l = Lark(grammar, start='r0')
  return l, messages


def main():
  l, messages = read()
  print("Part 1:", solve(l, messages))
  l, messages = read(part2=True)
  print("Part 2:", solve(l, messages))


if __name__ == "__main__":
  main()

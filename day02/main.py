#!/usr/bin/env python3

from collections import Counter, namedtuple
import re

pattern = re.compile(r'(\d+)-(\d+) (\w): (\w+)')
PasswordCheck = namedtuple('PasswordCheck', 'min max letter password')


def solve_part1(passwords):
  cnt = 0
  for pw in passwords:
    letters = Counter(pw.password)
    if pw.min <= letters[pw.letter] <= pw.max:
      cnt += 1
  return cnt


def solve_part2(passwords):
  cnt = 0
  for pw in passwords:
    if (pw.password[pw.min - 1] == pw.letter) + (pw.password[pw.max - 1] == pw.letter) == 1:
      cnt += 1
  return cnt

def main():
  passwords = []
  with open('input.txt', 'r') as f:
    lines = f.readlines()
  for line in lines:
    match = pattern.match(line)
    passwords.append(PasswordCheck(int(match.group(1)), int(
        match.group(2)), match.group(3), match.group(4)))

  print("Part 1:", solve_part1(passwords))
  print("Part 2:", solve_part2(passwords))


if __name__ == "__main__":
  main()

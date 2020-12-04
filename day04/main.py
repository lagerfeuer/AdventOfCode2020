#!/usr/bin/env python3

import re
height_re = re.compile(r'(\d+)(in|cm)')
hair_color_re = re.compile(r'^#[0-9a-f]{6}$')
pid_re = re.compile(r'^\d{9}$')


def validate_field(name, value):
  if name == 'byr':
    return (1920 <= int(value) <= 2002)
  elif name == 'iyr':
    return (2010 <= int(value) <= 2020)
  elif name == 'eyr':
    return (2020 <= int(value) <= 2030)
  elif name == 'hgt':
    if match := height_re.match(value):
      (val, unit) = match.groups()
      size = int(val)
      return (150 <= size <= 193) if unit == 'cm' else (59 <= size <= 76)
    else:
      return False
  elif name == 'hcl':
    return hair_color_re.match(value)
  elif name == 'ecl':
    return value in 'amb blu brn gry grn hzl oth'.split()
  elif name == 'pid':
    return pid_re.match(value)
  else:
    return True


def validate(p, strict=False):
  basic_check = len(p.keys()) == 8 or (
      len(p.keys()) == 7 and 'cid' not in p.keys())

  if strict:
    return basic_check and all(validate_field(key, val) for (key, val) in p.items())
  return basic_check


def solve_part1(passports):
  valid_passports = list(filter(validate, passports))
  return len(valid_passports)


def solve_part2(passports):
  valid_passports = list(filter(lambda x: validate(x, strict=True), passports))
  return len(valid_passports)


def read(file='input.txt'):
  with open(file, 'r') as f:
    raw_passport_data = [s.strip().replace('\n', ' ')
                         for s in f.read().split('\n\n')]

  return [
      {
          key: val
          for pair in raw_data.split(' ')
          for (key, val) in [pair.split(':')]
      }
      for raw_data in raw_passport_data
  ]


def main():
  passports = read()
  print("Part 1:", solve_part1(passports))
  print("Part 2:", solve_part2(passports))


if __name__ == "__main__":
  main()

#!/usr/bin/env python3

import re
from functools import reduce
from operator import mul, or_, and_

RULE_RE = re.compile(r'([a-z ]+): (\d+-\d+) or (\d+-\d+)')


def is_field_valid(rules, field):
  return any(is_field_in_range(field, *ranges[1:]) for ranges in rules)


def is_field_in_range(field, *ranges):
  return any(r[0] <= field <= r[1] for r in ranges)


def solve_part1(rules, tickets):
  errors = [field
            for ticket in tickets
            for field in ticket
            if not is_field_valid(rules, field)]
  return sum(errors)


def solve_part2(rules, tickets, my_ticket):
  valid_tickets = [ticket
                   for ticket in tickets
                   if all(is_field_valid(rules, field) for field in ticket)]

  # create an array of possible field names per ticket,
  # each field has a set of possible names according to the validity of values
  possible_field_names = [[set() for _ in range(len(valid_tickets))]
                          for _ in range(len(valid_tickets[0]))]
  for (tid, ticket) in enumerate(valid_tickets):
    for (fid, field) in enumerate(ticket):
      for (name, r1, r2) in rules:
        if is_field_in_range(field, r1, r2):
          possible_field_names[fid][tid].add(name)

  # there is one field that can be correctly identified.
  # by eliminating this field from all other possible fields,
  # we get another field we can correctly assign, and so on.
  # we continue this elimination process until all fields have been assigned.
  field_names = [reduce(and_, field) for field in possible_field_names]
  assigned = set()
  while any(len(f) > 1 for f in field_names):
    identified = reduce(or_, filter(lambda s: len(
        s) == 1 and s not in assigned, field_names))
    for i in identified:
      for f in field_names:
        if len(f) > 1 and i in f:
          f -= identified
      assigned.add(i)
  field_names = [e.pop() for e in field_names]

  # get the corresponding fields from my_ticket
  return reduce(mul, [my_ticket[idx]
                      for (idx, name) in enumerate(field_names)
                      if name.startswith('departure')])


def read(file='input.txt'):
  def parse_range(s):
    return tuple([int(x) for x in s.split('-')])

  with open(file, 'r') as f:
    (rules_in, my_ticket_in, tickets_in) = f.read().split('\n\n')

  rules = []
  for rule in rules_in.splitlines():
    (name, range1, range2) = RULE_RE.match(rule).groups()
    rules.append((name, parse_range(range1), parse_range(range2)))

  my_ticket = tuple(int(x) for x in my_ticket_in.split('\n')[-1].split(','))

  tickets = [tuple(int(x) for x in l.split(','))
             for l in tickets_in.splitlines()[1:]]

  return (rules, my_ticket, tickets)


def main():
  (rules, my_ticket, tickets) = read()
  print("Part 1:", solve_part1(rules, tickets))
  print("Part 2:", solve_part2(rules, tickets, my_ticket))


if __name__ == "__main__":
  main()

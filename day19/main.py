#!/usr/bin/env python3

from pyformlang.cfg import Production, Terminal, Variable, CFG


def solve(cfg, messages):
  return [cfg.contains(msg) for msg in messages].count(True)


def grammar(rules):
  terminals = set()
  variables = set()
  productions = set()

  for (k, v) in rules.items():
    variables.add(Variable(k))
    if isinstance(v, str):
      terminals.add(Terminal(v))
      productions.add(Production(Variable(k), [Terminal(v)]))
    else:
      for e in v:
        productions.add(Production(
            Variable(k), [Variable(x) for x in e]))

  cfg = CFG(variables, terminals, Variable('0'), productions)
  return cfg


def read(file='input.txt'):
  with open(file, 'r') as f:
    (rules, messages) = [[l.strip() for l in part.splitlines()]
                         for part in f.read().split('\n\n')]

  rules = {k: v[1:-1] if v.startswith('"') else [[e
                                                  for e in opts.split(' ')]
                                                 for opts in v.split(' | ')]
           for line in rules
           for (k, v) in [line.split(': ')]}

  return rules, messages


def main():
  rules, messages = read()
  extended = rules | {
      '8': [r.split() for r in '42 | 42 8'.split()],
      '11': [r.split() for r in '42 31 | 42 11 31'.split(' | ')]
  }
  print("Part 1:", solve(grammar(rules), messages))
  print("Part 2:", solve(grammar(extended), messages))


if __name__ == "__main__":
  main()

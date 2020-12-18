#!/usr/bin/env python3

from operator import add, mul
from abc import ABC, abstractmethod


class Node(ABC):
  def eval(self):
    pass


class Const(Node):
  def __init__(self, value):
    self.value = value

  def eval(self):
    return self.value

  def __str__(self):
    return str(self.value)


class BinaryOp(Node):
  def __init__(self, left, op, right):
    self.left = left
    self.op = add if op == '+' else mul
    self.op_str = op
    self.right = right

  def eval(self):
    return self.op(self.left.eval(), self.right.eval())

  def __str__(self):
    return f"({self.left} {self.op_str} {self.right})"


def solve(exprs):
  return sum(expr.eval() for expr in exprs)

def parse(line, prec):
  def const(stack):
    return Const(int(stack.pop()))

  def expr(stack):
    if stack[-1].isdigit():
      return const(stack)
    op = stack.pop()
    right = expr(stack)
    left = expr(stack)
    return BinaryOp(left, op, right)

  """https://en.wikipedia.org/wiki/Shunting-yard_algorithm"""
  out = []
  op_stack = []
  for tok in line:
    if tok.isdigit():
      out.append(tok)
    elif tok in list('+*'):
      while op_stack and op_stack[-1] != '(' and prec[op_stack[-1]] >= prec[tok]:
        out.append(op_stack.pop())
      op_stack.append(tok)
    elif tok == '(':
      op_stack.append(tok)
    elif tok == ')':
      while op_stack and op_stack[-1] != '(':
        out.append(op_stack.pop())
      if op_stack[-1] == '(':
        op_stack.pop()

  while op_stack:
    out.append(op_stack.pop())

  return expr(out)


def read(file='input.txt'):
  with open(file, 'r') as f:
    return [l.replace('(', '( ').replace(')', ' )').split(' ')
            for l in f.read().splitlines()]


def main():
  lines = read()
  exprs = [parse(l, {'+': 1, '*': 1}) for l in lines]
  print("Part 1:", solve(exprs))
  exprs = [parse(l, {'+': 2, '*': 1}) for l in lines]
  print("Part 2:", solve(exprs))


if __name__ == "__main__":
  main()

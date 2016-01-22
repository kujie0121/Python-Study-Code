#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(max):
      n, a, b =0, 0, 1
      while n < max:
            yield b
            a, b =b, a +b
            n =n +1
      return 'done'

f = fib(5)

while True:
      try:
            x = next(f)
            print(x)
      except StopIteration as e:
            print('Generator return value:', e.value)
            break
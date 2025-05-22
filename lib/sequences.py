#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        fib_list = [0, 1]
        while len(fib_list) < length:
            next_fib = fib_list[-1] + fib_list[-2]
            fib_list.append(next_fib)
        print(fib_list)
#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print("[]")
    elif length == 1:
        print("[0]")
    else:
        fibonacci_sequence = [0, 1]
        for i in range(2, length):
            next_fibonacci = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
            fibonacci_sequence.append(next_fibonacci)
        print(f"[{', '.join(map(str, fibonacci_sequence))}]")


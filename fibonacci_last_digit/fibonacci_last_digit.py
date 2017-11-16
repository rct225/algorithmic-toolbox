# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit_better(n):
    if n <= 1:
        return n
    
    f = []
    a = 0
    b = 1

    for i in range(n + 1):
        f.append(a % 10)
        a, b = b, (a + b) % 10

    return f[n]

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
#print(get_fibonacci_last_digit_naive(n))
    print(get_fibonacci_last_digit_better(n))
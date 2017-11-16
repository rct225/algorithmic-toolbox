# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def pisano(m):
    a = 0
    b = 1

    for i in range(0, m * m):
        a, b = b, (a + b) % m
        if a == 0 and b == 1:
            return i + 1


def calc_fib_better(n):
    # if (n <= 1):
        # return n

    f = []
    a = 0
    b = 1

    for i in range(n + 1):
        f.append(a)
        a, b = b, a + b

    return f[n]


def get_fibonacci_huge_better(n, m):
    if n <= 1:
        return n

    p = pisano(m)

    f_n_remainder = n % p

    last_digit = calc_fib_better(f_n_remainder) % m

    if last_digit == 0:
        return 10

    return last_digit


def fibonacci_sum_better(n):

    return get_fibonacci_huge_better(n + 2, 10) - 1


if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    # print(fibonacci_sum_naive(n))
    print(fibonacci_sum_better(n))

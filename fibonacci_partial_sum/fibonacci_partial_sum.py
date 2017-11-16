# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

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

    return last_digit


def fibonacci_sum_better(n):
    test = get_fibonacci_huge_better(n + 2, 10) - 1

    # print("FSB: " + str(n) + " " + str(test))

    return test


def fibonacci_partial_sum_better(from_, to):
    if from_ == to:
        return get_fibonacci_huge_better(from_, 10)

    result = fibonacci_sum_better(to) - fibonacci_sum_better(from_ - 1)

    if result < 0:
        return result + 10

    return result


if __name__ == '__main__':
    input = sys.stdin.readline()
    from_, to = map(int, input.split())
    # print(fibonacci_partial_sum_naive(from_, to))
    print(fibonacci_partial_sum_better(from_, to))

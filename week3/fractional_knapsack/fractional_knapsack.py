# Uses python3

import sys


def ratio(item):
    return float(item[0] / item[1])


def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    value_weights = zip(values, weights)
    value_weights = [list(elem) for elem in
                     sorted(value_weights, key=ratio, reverse=True)]

    A = [0] * len(weights)
    value = 0
    for i in range(len(weights)):
        if capacity == 0:
            return value
        a = min(value_weights[i][1], capacity)
        value = value + a * (float(value_weights[i][0]) / value_weights[i][1])
        value_weights[i][1] = value_weights[i][1] - a
        A[i] = A[i] + a
        capacity = capacity - a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    # print(data)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

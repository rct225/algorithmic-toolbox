# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


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


n = int(input())
print(calc_fib_better(n))

# for i in range(1000):
#     res1 = calc_fib(i)
#     res2 = calc_fib_better(i)
#
#     if res1 == res2:
#         print(str(res1) + " " + str(res2) + " OK")
#     else:
#         print("ERROR " + str(res1) + " " + str(res2))
#         break

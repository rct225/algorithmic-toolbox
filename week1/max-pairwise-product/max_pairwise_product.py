# Uses python3
# import random

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)


def max_pairwise_product_naive(a, n):
    result = 0

    for i in range(0, n):
        for j in range(i + 1, n):
            if a[i] * a[j] > result:
                result = a[i] * a[j]

    return result


def max_pairwise_product_faster(a, n):
    result = 0
    first = second = 0
    # max_index1 = -1
    # max_index2 = -1

    for i in range(0, n):
        if first < a[i]:
            second = first
            first = a[i]
            # max_index1 = i

        elif (second < a[i]):
            second = a[i]
            # max_index2 = i

    # print(str(max_index1) + " " + str(max_index2))
    result = first * second
    return result


print(max_pairwise_product_faster(a, n))

# while (True):
#     # n = random.randint(2, 11)
#     n = random.randint(2,5)
#     a = []
#     for i in range(0, n):
#         # a.append(random.randint(0, 100000))
#         a.append(random.randint(0,10))
#     print(a)
#     res1 = max_pairwise_product_naive(a, n)
#     res2 = max_pairwise_product_faster(a, n)
#
#     if res1 != res2:
#         print("Wrong answer: " + str(res1) + " " + str(res2))
#         break
#     else:
#         print("OK")

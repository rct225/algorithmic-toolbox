# Uses python3


def get_change(m):
    num_coins = 0
    # write your code here
    num_coins, r = divmod(m, 10)
    for i in (5, 1):
        nc, r = divmod(r, i)
        num_coins += nc

    return num_coins


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))

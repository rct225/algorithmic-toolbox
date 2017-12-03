# Uses python3


class cmpclass(object):
    def __init__(self, n):
        self.n = str(n)

    def __str__(self):
        return self.n

    def _cmp(self, other):
        a, b = self.n, str(other)
        ab, ba = a + b, b + a
        if ab == ba:
            return 0
        if ab < ba:
            return -1
        return 1

    def __lt__(self, other):
        return self._cmp(other) == -1

    def __le__(self, other):
        return self._cmp(other) <= 0

    def __eq__(self, other):
        return self._cmp(other) == 0

    def __ne__(self, other):
        return self._cmp(other) != 0

    def __gt__(self, other):
        return self._cmp(other) == 1

    def __ge__(self, other):
        return self._cmp(other) >= 0


def largest_number(data):
    data.sort(key=cmpclass, reverse=True)
    return "".join(data)


if __name__ == '__main__':
    n = int(input())
    data = input().split()
    # print(a)
    print(largest_number(data))

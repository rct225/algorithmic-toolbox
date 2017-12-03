# Uses python3
from operator import attrgetter
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    # write your code here
    sorted_segments = sorted(segments, key=attrgetter('end'))
    current = sorted_segments[0].end
    points.append(current)
    for s in sorted_segments:
        if current < s.start or current > s.end:
            current = s.end
            points.append(current)
    return points


if __name__ == "__main__":
    # input = sys.stdin.read()
    n = int(input())
    data = []
    for i in range(n):
        x, y = map(int, input().split())
        data.append((x, y))
    # print(data)
    segments = list(
        map(lambda x: Segment(x[0], x[1]), data))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=" ")

# 최대 힙
import sys
import heapq
# sys.stdin = open('../input.txt', 'r')


N = int(sys.stdin.readline())
pq = []
for _ in range(N):
    a = int(sys.stdin.readline())
    if a == 0:
        if len(pq) == 0:
            print(0)
        else:
            print((-1) * heapq.heappop(pq))
    else:
        heapq.heappush(pq, (-1) * a)

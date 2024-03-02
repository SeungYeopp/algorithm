# 카드 정렬하기
import sys
import heapq
# sys.stdin = open('../input.txt', 'r')


N = int(sys.stdin.readline())
pq = []
for i in range(N):
    heapq.heappush(pq, int(sys.stdin.readline()))
sum_val = 0


while len(pq) >= 2:
    a1 = heapq.heappop(pq)
    a2 = heapq.heappop(pq)
    sum_val += a1 + a2
    heapq.heappush(pq, a1 + a2)

print(sum_val)

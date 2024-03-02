# 케빈 베이컨의 6단계 법칙
import sys
from collections import deque
# sys.stdin = open('../input.txt', 'r')


N, M = map(int, input().split(" "))
graph = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)


def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        target = q.popleft()

        for i in graph[target]:
            if not visited[i]:
                visited[i] = visited[target] + 1
                q.append(i)

ans = []
for i in range(1, N + 1):
    visited = [0] * (N + 1)
    bfs(i)
    ans.append(sum(visited))

print(ans.index(min(ans)) + 1)
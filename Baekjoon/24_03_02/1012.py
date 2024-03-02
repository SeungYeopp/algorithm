# 유기농 배추
import sys
from collections import deque
# sys.stdin = open('../input.txt', 'r')


T = int(input())


for _ in range(T):
    M, N, K = map(int, input().split(" "))
    graph = [[0] * M for _ in range(N)]
    arr = []
    visited = [[0] * M for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    cnt = 0

    for i in range(K):
        arr.append(list(map(int, input().split(" "))))

    for x, y in arr:
        graph[y][x] = 1

    def bfs(i, j):
        q = deque()
        q.append((i, j))
        while q:
            cur_x, cur_y = q.popleft()

            for i in range(4):
                next_x, next_y = cur_x + dx[i], cur_y + dy[i]

                if next_x >= 0 and next_y >= 0 and next_x < M and next_y < N:
                    if graph[next_y][next_x] == 1 and visited[next_y][next_x] == 0:
                        visited[next_y][next_x] = 1
                        q.append((next_x, next_y))

    for ii in range(N):
        for jj in range(M):
            if not visited[ii][jj] and graph[ii][jj] == 1:
                visited[ii][jj] = 1
                bfs(jj, ii)
                cnt += 1

    print(cnt)
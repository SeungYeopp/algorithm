# 미로 탐색
import sys
from collections import deque
# sys.stdin = open('../input.txt', 'r')



n, m = map(int, input().split(" "))
graph = []
visited = [[0] * m for _ in range(n)]
cnt = 0
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((0, 0))
visited[0][0] = 1

while q:
    cur_x, cur_y = q.popleft()

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        if nx >= 0 and nx < m and ny >= 0 and ny < n:
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                cnt += 1
                visited[ny][nx] = visited[cur_y][cur_x] + 1
                q.append((nx, ny))


print(visited[n-1][m-1])
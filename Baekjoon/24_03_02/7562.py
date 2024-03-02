# 나이트의 이동
import sys
from collections import deque
# sys.stdin = open('../input.txt', 'r')


T = int(input())
ans = []
for _ in range(T):
    l = int(input())
    visited = [[-1] * l for _ in range(l)]
    x, y = map(int, input().split(" "))
    f_x, f_y = map(int, input().split(" "))
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]

    q = deque()
    q.append((x, y))
    visited[x][y] = 0

    while q:
        cur_x, cur_y = q.popleft()
        if cur_x == f_x and cur_y == f_y:
            print(visited[f_x][f_y])
            break

        for i in range(8):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]

            if next_x >= 0 and next_y >= 0 and next_x < l and next_y < l:
                if visited[next_x][next_y] == -1:
                    visited[next_x][next_y] = visited[cur_x][cur_y] + 1
                    q.append((next_x, next_y))



# 직사각형 네개의 합집합의 면적 구하기
import sys
sys.stdin = open("input.txt", 'r')


arr = []
visited = [[0] * 100 for _ in range(100)]
cnt = 0

for i in range(4):
    arr.append(list(map(int, input().split(" "))))

for x1, y1, x2, y2 in arr:
    for i in range(100):
        for j in range(100):
            if x1 <= i < x2 and y1 <= j < y2:
                if not visited[i][j]:
                    cnt += 1
                    visited[i][j] = 1

print(cnt)
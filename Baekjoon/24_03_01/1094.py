# 막대기
import sys
sys.stdin = open("input.txt", 'r')


X = int(input())
arr = [64, 32, 32, 16, 16, 8, 8, 4, 4, 2, 2, 1, 1]

ans = 0
cnt = 0
for a in arr:
    if X >= a:
        ans += a
        X -= a
        cnt += 1

    if X == 0:
        break

print(cnt)

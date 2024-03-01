# 수 정렬하기
import sys
sys.stdin = open("input.txt", 'r')


N = int(input())
ans = []
for i in range(N):
    ans.append(int(input()))

ans.sort()
for i in ans:
    print(i)
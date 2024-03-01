# 다각형의 대각선
import sys
sys.stdin = open("input.txt", 'r')


N = int(input())

print(N*(N-1)*(N-2)*(N-3) // 24)
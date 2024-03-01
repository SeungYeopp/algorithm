# Yangjojang of The Year
import sys
sys.stdin = open("input.txt", 'r')

T = int(input())


while T:
    arr = []
    res = 0
    ans = ""
    N = int(input())
    for _ in range(N):
        arr.append(list(map(str, input().split(" "))))

    for a in arr:
        if res <= int(a[1]):
            res = int(a[1])
            ans = a[0]

    print(ans)
    T -= 1
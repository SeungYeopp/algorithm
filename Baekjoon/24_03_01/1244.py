# 스위치 켜고 끄기
import sys
sys.stdin = open("input.txt", 'r')


arr = []
N = int(input())
switches = list(map(int, input().split(" ")))
num_person = int(input())

for _ in range(num_person):
    arr.append(list(map(int, input().split(" "))))

for i in range(num_person):
    if arr[i][0] == 1:
        n = N // arr[i][1]
        for j in range(1, n+1):
            switches[arr[i][1]*j-1] ^= 1

    else:
        idx = arr[i][1] - 1
        switches[idx] ^= 1
        left = idx - 1
        right = idx + 1
        while left >= 0 and right < N and switches[left] == switches[right]:
            switches[left] ^= 1
            switches[right] ^= 1
            left -= 1
            right += 1

for k in range(1,N+1):
    print(switches[k-1], end=" ")
    if k % 20 == 0:
        print()
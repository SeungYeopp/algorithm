# 경비원
import sys
sys.stdin = open('input.txt', 'r')


n, m = map(int, input().split(" "))
N = int(input())
arr = []
new_arr = []
cnt = 0
for _ in range(N+1):
    arr.append(list(map(int, input().split(" "))))

for a in arr:
    if a[0] == 1:
        new_arr.append([a[1], m])
    elif a[0] == 2:
        new_arr.append([a[1], 0])
    elif a[0] == 3:
        new_arr.append([0, m-a[1]])
    else:
        new_arr.append([n, m-a[1]])

x, y = new_arr[-1][0], new_arr[-1][1]

for aa in new_arr:
    if (x == n and aa[0] == n) or (x == 0 and aa[0] == 0):
        cnt += abs(y - aa[1])
    elif (y == m and aa[1] == m) or (y == 0 and aa[1] == 0):
        cnt += abs(x - aa[0])
    elif (y == 0 and aa[1] == m) or (y == m and aa[1] == 0):
        cnt += min(x + m + aa[0], 2 * (m+n) - (x + m + aa[0]))
    elif (x == 0 and aa[0] == n) or (x == n and aa[0] == 0):
        cnt += min(y + n + aa[1], 2 * (m+n) - (y + n + aa[1]))
    else:
        cnt += abs(x-aa[0]) + abs(y-aa[1])

print(cnt)


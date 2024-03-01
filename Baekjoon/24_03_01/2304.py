# 창고 다각형
import sys
sys.stdin = open("input.txt", 'r')


N = int(input())

arr = []
cnt = 0
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr1 = sorted(arr, key = lambda x: x[0])
arr2 = sorted(arr, key = lambda x: x[0], reverse = True)
max_val = max(arr, key = lambda x: x[1])

x, y = arr1.pop(0)
xx, yy = arr2.pop(0)
cnt += max_val[1]


for x1, y1 in arr1:
    if x1 > max_val[0]:
        break

    if y1 >= y:
        cnt += (x1 - x) * y
        x = x1
        y = y1
    else:
        continue

for x2, y2 in arr2:
    if x2 < max_val[0]:
        break
    if yy <= y2:
        cnt += (xx - x2) * yy
        xx = x2
        yy = y2

    else:
        continue

print(cnt)

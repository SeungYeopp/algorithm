# 통계학
import sys
sys.stdin = open("input.txt", 'r')


N = int(input())
arr = []
x = {}
arr2 = []

for _ in range(N):
    arr.append(int(input()))
arr.sort()
for i in arr:
    if i in x:
        x[i] += 1
    else:
        x[i] = 1
max_val = max(x.values())

for key in x:
    if x[key] == max_val:
        arr2.append(key)
if len(arr2) > 1:
    c = arr2[1]
else:
    c = arr2[0]

a = round(sum(arr)/N)
b = arr[N//2]
d = max(arr) - min(arr)

print(a)
print(b)
print(c)
print(d)
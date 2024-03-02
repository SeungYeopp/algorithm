# 셀프 넘버
# import sys
# sys.stdin = open('../input.txt', 'r')

x = 1
ans = list(range(1, 10001))

while x <= 10000:
    num = list(str(x))
    arr = x
    for i in range(len(num)):
        arr += int(num[i])

    if arr in ans:
        ans.remove(arr)

    x += 1


for i in range(len(ans)):
    print(ans[i])

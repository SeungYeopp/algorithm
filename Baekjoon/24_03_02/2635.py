# 수 이어가기
# import sys
# sys.stdin = open('../input.txt', 'r')

def check(N, num):
    n_list = [N, num]
    while True:
        x = N - num
        if x < 0:
            break
        n_list.append(x)
        N = num
        num = x
    return n_list

N = int(input())
num = N
max_list = []
while True:
    ch = check(N, num)
    if len(max_list) < len(ch):
        max_list = ch
    num -= 1
    if num < 0:
        break

print(len(max_list))
print(*max_list)

# AC
import sys
from collections import deque
sys.stdin = open('../input.txt', 'r')


T = int(sys.stdin.readline())

for _ in range(T):
    cmd = sys.stdin.readline().rstrip()
    n = int(input())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    if n == 0:
        arr = deque()
    cnt = 0

    for c in cmd:
        if c == 'R':
            cnt += 1

        else:
            if len(arr) == 0:
                print('error')
                break
            if cnt % 2 == 0:
                arr.popleft()
            else:
                arr.pop()


    else:
        if cnt % 2 == 1:
            arr.reverse()
        print("["+",".join(arr)+"]")

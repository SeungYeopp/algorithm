# 괄호 끼워넣기
import sys
sys.stdin = open("input.txt", 'r')


S = input()
stack = []
cnt = 0
for s in S:
    if s == "(":
        stack.append(")")
    elif len(stack) and s == ")":
        stack.pop()
    else:
        cnt += 1

print(cnt + len(stack))
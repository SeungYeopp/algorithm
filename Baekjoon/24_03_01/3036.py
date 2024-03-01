# 링
import sys
sys.stdin = open("input.txt", 'r')


N = int(input())
nums = list(map(int, input().split(" ")))

first_num = nums.pop(0)
for num in nums:
    if first_num % num == 0:
        print((first_num//num),"/",1, sep="")

    else:
        for i in range(num, 0, -1):
            if (first_num % i == 0) and (num % i == 0):
                x = i
                break
        print((first_num//x),"/",(num//x), sep="")

# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 경우의 수를 구하는 문제
# 재귀함수를 이용해 해결

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def three(n) :
    if n == 1 :
        return 1
    elif n == 2 :
        return 2
    elif n == 3 :
        return 4
    else :
        return three(n - 1) + three(n - 2) + three(n - 3)

num_test = int(input())

for i in range(num_test) :
    num = int(input())
    print(three(num))

# 정답
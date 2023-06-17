# N이 주어졌을 때, 파도반 수열 P(N)을 구하는 문제
# 재귀함수를 이용하여 해결

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

num_tests = int(input())
for i in range(num_tests) :
    p = [1, 1, 1, 2, 2]
    target = int(input())
    if target > 5 :
        for j in range(5, target) :
            p.append(p[j - 1] + p[j - 5])
    print(p[target - 1])

# 정답.
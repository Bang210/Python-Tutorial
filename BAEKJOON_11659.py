# N개의 수가 주어졌을 때, i번째 수부터 j번째 수까지의 합을 구하는 문제

import sys
input = sys.stdin.readline

num_numbers, num_tests = map(int, input().split())
nums = list(map(int, input().split()))
sums = list(0 for _ in range(num_numbers))

for i in range(num_numbers) :
    if i == 0 :
        sums[i] = nums[i]
    else :
        sums[i] = sums[i - 1] + nums[i]

for j in range(num_tests) :
    start, end = map(int, input().split())
    start -= 1
    end -= 1
    if start == end :
        print(nums[end])
    elif start == 0 :
        print(sums[end])
    else :
        print(sums[end] - sums[start - 1])

# 정답
# 주어진 N개의 수를 오름차순으로 정렬하는 문제

import sys
input = sys.stdin.readline

test_num = int(input())
arr = list(0 for i in range(10001))

for j in range(test_num) :
    test = int(input())
    arr[test] += 1

for k in range(len(arr)) :
    if arr[k] != 0:
        for l in range(arr[k]) :
            print(k)

# 정답
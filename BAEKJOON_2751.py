# 첫째 줄에 주어지는 수 N 만큼의 정수가 주어질 때, 오름차순으로 정렬하여 출력하는 문제

import sys
input = sys.stdin.readline
arr = list()
num = int(input())

for _ in range(num) :
    arr.append(int(input()))

arr.sort()

for i in range(num) :
    print(arr[i])

# 정답
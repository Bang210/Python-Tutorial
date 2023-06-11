# 3으로 나눔 / 2로 나눔 / 1을 뺌 세가지 연산을 통해 주어진 수를 1로 만들 때, 연산의 최소 횟수를 구하는 문제
# 다이나믹 프로그래밍

import sys
input = sys.stdin.readline
num = int(input())

arr = [0 for i in range(num + 1)]

for j in range(num + 1) :
    if j == 0 or j == 1 :
        pass
    elif j % 3 == 0 and j % 2 == 0 :
        arr[j] = min(arr[j // 2], arr[j // 3], arr[j - 1]) + 1
    elif j % 3 == 0 and j % 2 != 0 :
        arr[j] = min(arr[j // 3], arr[j - 1]) + 1
    elif j % 3 != 0 and j % 2 == 0 :
        arr[j] = min(arr[j // 2], arr[j - 1]) + 1
    else :
        arr[j] = arr[j - 1] + 1

print(arr[num])

# 정답.
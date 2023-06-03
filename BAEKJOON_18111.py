# B개의 블록을 보유한 상태에서 각 좌표에서의 높이가 주어진 M x N 넓이의 땅을 고르게 만들 때, 제거는 2초 설치는 1초가 걸린다는 조건에서 작업의 최소시간을 구하는 문제.

import sys
input = sys.stdin.readline

length, width, inventory = map(int, input().split())
land = list()
current = dict()
cnt = 0

for i in range(length) :
    arr = list(map(int, input().split()))
    for j in range(width) :
        if arr[j] in current :
            current[arr[j]] += 1
        else :
            current[arr[j]] = 1

bottom = min(current.keys())
top = max(current.keys())

while current[top] < length * width :
    dig_time = current[top] * 2
    stack_time = current[bottom]

    if dig_time >= stack_time and inventory >= stack_time :
        cnt += stack_time
        inventory -= current[bottom]
        if bottom + 1 in current :
            current[bottom + 1] += current[bottom]
        else :
            current[bottom + 1] = current[bottom]
        del current[bottom]
        bottom += 1

    else :
        cnt += dig_time
        inventory += current[top]
        if top - 1 in current :
            current[top - 1] += current[top]
        else :
            current[top - 1] = current[top]
        del current[top]
        top -= 1

print(cnt, max(current))

# 정답.
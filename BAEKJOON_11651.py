# N개의 2차원 좌표에 대해, y좌표의 오름차순, x좌표의 오름차순의 우선순위로 정렬하는 문제

import sys
input = sys.stdin.readline

test_num = int(input())
test = list()

for i in range(test_num) :
    x, y = map(int, input().split())
    test.append((x, y,))

test.sort(key = lambda x : (x[1], x[0]))
print(test)
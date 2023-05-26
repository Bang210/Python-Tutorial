# 입력받은 N개의 좌표에 대해 x의 오름차순, y의 오름차순 순서의 우선순위로 정렬하는 문제

import sys
input = sys.stdin.readline

test = list()
test_num = int(input())
for i in range(test_num) :
    a, b = map(int, input().split())
    test.append((a, b,))

answer = sorted(test)
for j in range(test_num) :
    print("{} {}".format(answer[j][0], answer[j][1]))

# 튜플 자료형 활용
# 정답.
# n번째 피보나치 수를 구하는 재귀함수 fibonacci(n)에서, 0과 1이 출력된 횟수를 구하는 문제

import sys
input = sys.stdin.readline


for i in range(int(input())) :
    num = int(input())
    cnt_0 = [1, 0, 1]
    cnt_1 = [0, 1, 1]
    if num >= 3 :
        for k in range(2, num) :
            cnt_0.append(cnt_0[k - 1] + cnt_0[k])
            cnt_1.append(cnt_1[k - 1] + cnt_1[k])
    print(cnt_0[num], cnt_1[num])

# 정답
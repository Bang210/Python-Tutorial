# 첫 줄에 주어진 수 T개의 테스트 데이터가 주어질 때, 각각 올바른 괄호 문자열인지 판별하는 문제

import sys
input = sys.stdin.readline

n = int(input())
result = list()

for i in range(n) :
    left = 0
    right = 0
    test = input().strip()
    for j in range(len(test)) :
        if test[j] == '(' :
            right += 1
        else :
            left += 1
            if left > right :
                check = 'NO'
                break
    if right == left :
        check = 'YES'
    else :
        check = 'NO'
    print(check)

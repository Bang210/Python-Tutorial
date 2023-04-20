# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
    
universe_num = int(input())
universe = sorted(list(map(int, input().split())))
test_num = int(input())
test = list(map(int, input().split()))

for i in range(test_num) :  
    first_num = 0
    last_num = len(universe) - 1
    while True :
        middle_num = (first_num + last_num) // 2
        if test[i] == universe[middle_num] :
            check = 1
            break
        elif (test[i] < universe[first_num]) or (test[i] > universe[last_num]) :
            check = 0
            break
        elif test[i] > universe[middle_num] :
            first_num = middle_num + 1
        else :
            last_num = middle_num
    print(check)

# 시간초과. arr리스트를 슬라이싱하는 과정에서 시간이 초과된 것으로 보임.
# 슬라이싱을 통해 리스트 자체를 수정하는 방법 대신, 기존 리스트의 탐색 범위를 새롭게 설정하는 방법으로 해결.
# 정답.
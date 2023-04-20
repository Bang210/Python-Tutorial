# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
    
universe_num = int(input())
universe = sorted(list(map(int, input().split())))
test_num = int(input())
test = list(map(int, input().split()))

for i in range(test_num) :
    arr = universe.copy()
    while True :
        middle_num = int((len(arr) - 1) * 0.5)
        middle = arr[middle_num]
        if test[i] == middle :
            check = 1
            break
        elif (test[i] < arr[0]) or (test[i] > arr[len(arr) - 1]) :
            check = 0
            break
        elif test[i] > middle :
            arr = arr[middle_num + 1 : ]
        else :
            arr = arr[ : middle_num]
    print(check)

# 시간초과. arr리스트를 슬라이싱하는 과정에서 시간이 초과된 것으로 보임.
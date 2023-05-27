# 큐를 구현하는 문제

import sys
input = sys.stdin.readline

test_num = int(input())
que_list = list()

for i in range(test_num) :
    command = input().rstrip()
    if command[0:4] == 'push' :
        num = int(command[5:])
        que_list.append(num)
    elif command == 'pop' :
        if len(que_list) == 0 :
            print(-1)
        else :
            print(que_list[0])
            del que_list[0]
    elif command == 'size' :
        print(len(que_list))
    elif command == 'empty' :
        if len(que_list) == 0 :
            print(1)
        else :
            print(0)
    elif command == 'front' :
        if len(que_list) == 0 :
            print(-1)
        else :
            print(que_list[0])
    elif command == 'back' :
        if len(que_list) == 0 :
            print(-1)
        else :
            print(que_list[len(que_list) - 1])

# 정답
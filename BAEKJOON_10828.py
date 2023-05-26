# 스택을 구현하는 문제

import sys
input = sys.stdin.readline

test_num = int(input())
stack = list()

for i in range(test_num) :
    command = input().rstrip()
    if command[0:4] == 'push' :
        x = int(command[5:])
        stack.append(x)
    elif command == 'pop' :
        if len(stack) != 0 :
            print(stack.pop())
        else :
            print(-1)
    elif command == 'size' :
        print(len(stack))
    elif command == 'empty' :
        if len(stack) == 0 :
            emptyness = 1
        else :
            emptyness = 0
        print(emptyness)
    elif command == 'top' :
        if len(stack) != 0 :
            print(stack[-1])
        else :
            print(-1)

# 정답
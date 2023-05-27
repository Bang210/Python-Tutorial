# 덱을 구현하는 문제

import sys
input = sys.stdin.readline
from collections import deque

test_num = int(input())
deq = deque()

for i in range(test_num) :
    command = input().rstrip()
    if 'push_front' in command :
        num = int(command[11:])
        deq.appendleft(num)
    elif 'push_back' in command :
        num = int(command[10:])
        deq.append(num)
    elif command == 'pop_front' :
        if len(deq) == 0 :
            print(-1)
        else :
            print(deq.popleft())
    elif command == 'pop_back' :
        if len(deq) == 0 :
            print(-1)
        else :
            print(deq.pop())
    elif command == 'size' :
        print(len(deq))
    elif command == 'empty' :
        if len(deq) == 0 :
            print(1)
        else :
            print(0)
    elif command == 'front' :
        if len(deq) == 0 :
            print(-1)
        else :
            print(deq[0])
    elif command == 'back' :
        if len(deq) == 0 :
            print(-1)
        else :
            print(deq[len(deq) - 1])

# 정답
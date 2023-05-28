# 정수를 연속으로 더하며 0이 주어질 때에는 최근의 값을 취소하는 문제

import sys
input = sys.stdin.readline

test_num = int(input())
test = list()

for i in range(test_num) :
    num = int(input())
    if num != 0 :
        test.append(num)
    else :
        del test[len(test) - 1]

print(sum(test))

# 정답
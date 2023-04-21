# 보유한 N개의 숫자카드(2번째 줄에 주어짐)에 대해, 정수 M개가 주어졌을 때 이중 몇 개를 가지고 있는지 구하는 문제

import sys
input = sys.stdin.readline

num = int(input())
card = list(map(int, input().split()))
card_set = sorted(list(set(card)))
test_num = int(input())
test = list(map(int, input().split()))
card_num = len(card_set)
result = list()

for i in range(test_num) :
    first = 0
    end = card_num - 1
    count = 0
    while True :
        middle = (first + end) // 2
        if test[i] < card_set[first] or test[i] > card_set[end] :
            break
        elif test[i] == card_set[middle] :
            count = card.count(test[i])
            break
        elif test[i] < card_set[middle] :
            end = middle
        else :
            first = middle + 1
    result.append(count)
for j in range(test_num) :
    print(result[j], end = ' ')

# 시간초과.
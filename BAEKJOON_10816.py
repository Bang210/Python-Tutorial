# 보유한 N개의 숫자카드(2번째 줄에 주어짐)에 대해, 정수 M개가 주어졌을 때 이중 몇 개를 가지고 있는지 구하는 문제

import sys
input = sys.stdin.readline

own_num = int(input())
own_list = list(map(int, input().split()))
test_num = int(input())
test_list = list(map(int, input().split()))
test_dict = {}

for i in range(test_num) :
    test_dict[test_list[i]] = 0

for j in range(own_num) :
    if own_list[j] in test_dict :
        test_dict[own_list[j]] += 1

for k in range(test_num) :
    print(test_dict[test_list[k]], end=' ')

# 이진탐색이 아닌 딕셔너리를 이용하는 방법으로 접근.
# 정답.
# 입력받은 N개의 단어에 대해 중복을 제거한 후 길이순, 사전순의 우선순위로 정렬하는 문제

import sys
input = sys.stdin.readline

test_num = int(input())
test_list = list()
for i in range(test_num) :
    test_list.append(input().rstrip())

test_list = list(set(test_list))
ans_list = sorted(test_list, key = lambda x : (len(x), x))

for j in range(len(ans_list)) :
    print(ans_list[j])

# sort와 lambda에 대한 공부
# 정답
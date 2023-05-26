# 나이와 이름이 주어지는 N개의 테스트케이스에 대해 나이의 오름차순, 입력순서의 우선순위로 정렬하는 문제

import sys
input = sys.stdin.readline

test_num = int(input())
member_list = list()
for i in range(test_num) :
    a, b = input().rstrip().split()
    member_list.append((int(a), b,))

member_list.sort(key = lambda x : x[0])

for j in range(test_num) :
    print("{} {}".format(member_list[j][0], member_list[j][1]))

# 정답
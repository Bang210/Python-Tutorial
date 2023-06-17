# 듣도 못한 사람의 명단과 보도 못한 사람의 명단이 차례로 주어질 때 듣도 보도 못한 사람의 명단을 구하는 문제

import sys
input = sys.stdin.readline

num_unheard, num_unseen = map(int, input().split())
unheard = list()
arr = list()

for i in range(num_unheard) :
    unheard.append(input().rstrip())

for j in range(num_unseen) :
    name = input().rstrip()
    if name in unheard :
        arr.append(name)

arr.sort()

print(len(arr))

for person in arr :
    print(person)
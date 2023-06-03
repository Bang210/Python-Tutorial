# 각각의 길이가 주어진 N개의 랜선을 잘라 같은 길이의 랜선 M개를 만들 때, 만드는 랜선 길이의 최대값을 구하는 문제

import sys
input = sys.stdin.readline

given, goal = map(int, input().split())
lans = list()

for i in range(given) :
    lans.append(int(input()))

start, end = 1, max(lans)

while start <= end :
    mid = (start + end) // 2
    cnt = 0
    for lan in lans :
        cnt += lan // mid
    if cnt >= goal :
        start = mid + 1
    else :
        end = mid - 1

print(end)

# 정답
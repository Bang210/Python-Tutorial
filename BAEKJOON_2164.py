# 순서대로 쌓인 1부터 N까지의 카드에 대해, [바닥카드 버림 -> 제일 위 카드 맨 아래로 보냄]을 반복해 마지막에 남는 카드를 구하는 문제.

import sys
input = sys.stdin.readline
num = int(input())

if num > 1 :
    card = list(i+ 2 for i in range(0, num, 2))       #첫 번째 사이클 생략
    while len(card) > 1 :
        for j in range(0, len(card), 2) :
            card[j] = 0
        card = list(set(card))
        card.remove(0)
else :
    card = [1]
print(card[0])

# pop을 이용해 압축을 시도했으나 시간초과.
# 요소를 하나씩 제거하는 과정에서 긴 시간이 소요된 것으로 보임.
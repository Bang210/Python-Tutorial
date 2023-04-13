# 순서대로 쌓인 1부터 N까지의 카드에 대해, [바닥카드 버림 -> 제일 위 카드 맨 아래로 보냄]을 반복해 마지막에 남는 카드를 구하는 문제.

import sys
input = sys.stdin.readline

card = list(i + 1 for i in range(int(input())))
while len(card) > 1 :
    del card[0]
    card.append(card[0])
    del card[0]

print(card[0])

# 시간초과.
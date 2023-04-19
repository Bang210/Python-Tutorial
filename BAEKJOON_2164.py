# 순서대로 쌓인 1부터 N까지의 카드에 대해, [바닥카드 버림 -> 제일 위 카드 맨 아래로 보냄]을 반복해 마지막에 남는 카드를 구하는 문제.

import sys
input = sys.stdin.readline
from collections import deque

card = deque(i + 1 for i in range(int(input())))

while len(card) > 1 :
	card.popleft()
	card.append(card.popleft())
	
print(card[0])

#문제에 대한 접근이 잘못된 것으로 보임.
#처음의 방법으로 돌아가되, deque 객체를 이용하여 시간단축.
#정답.
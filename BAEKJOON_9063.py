# 주어진 좌표들을 포함하는 가장 작은 정사각형의 넓이를 구하는 문제

import sys
input = sys.stdin.readline

n = int(input())
x = list()
y = list()

for i in range(n) :
	a, b = map(int, input().split())
	x.append(a)
	y.append(b)
	
width = max(x) - min(x)
length = max(y) - min(y)

land = width * length

print(land)

# 정답
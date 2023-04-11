# 연립방정식   {ax + by = c} 에 대해 a, b, c, d, e가 주어졌을 때 해(x, y)를 구하는 문제
#             {dx + ey = f}

import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

x = int((e * c - b * f) / (a * e - b * d))
y = int((d * c - a * f) / (b * d - a * e))

print(x, y)

# 정답
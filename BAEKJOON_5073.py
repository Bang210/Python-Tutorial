# 세 변의 길이가 주어졌을 때 어떤 삼각형인지 판별하는 문제

def triangle(a, b, c) :
	if a >= b + c or b >= c + a or c >= a + b  :
		return 'Invalid'
	elif a == b == c :
		return 'Equilateral'
	elif a == b or b == c or c == a :
		return 'Isosceles'
	else :
		return 'Scalene'
		
while True :
	x, y, z = map(int, input().split())
	if x == y == z == 0 :
		break
	else :
		print(triangle(x, y, z))
		
# 정답
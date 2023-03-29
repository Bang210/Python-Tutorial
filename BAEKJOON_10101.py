# 세 각의 크기가 주어졌을 때 삼각형의 종류를 판별하는 문제

a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180 :
	value = 'Error'
elif a == b or b == c or c == a :
	if a == 60 :
		value = 'Equilateral'
	else :
		value = 'Isosceles'
else :
	value = 'Scalene'
	
print(value)

# 정답
# 주어진 자연수 n을 4개 이하의 제곱수로 표현할 때, 필요한 제곱수의 최소값을 구하는 문제

import sys
input = sys.stdin.readline

num = int(input())
root = int(num ** 0.5)
roots_list = list()

for i in range(1, root + 1) :
    roots_list.append( i ** 2)

def sol() :
    if root == num ** 0.5 :
        return 1
    for j in range(1, root + 1) :
        if num - j ** 2 in roots_list :
            return 2
    for k in range(root + 1) :
        for l in range(root + 1) :
            if num - k ** 2 - l ** 2 in roots_list :
                return 3
    return 4

print(sol())

# 정답
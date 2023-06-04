# 서로 다른 조합의 개수를 찾는 문제
 
import sys
input = sys.stdin.readline

test_case = int(input())

for i in range(test_case) :
    num_items = int(input())
    dic = dict()
    ans = 1
    for j in range(num_items) :
        item, part = input().rstrip().split()
        if part in dic :
            dic[part] += 1
        else :
            dic[part] = 1
    arr = list(dic.values())
    for element in arr :
        ans = ans * (element + 1)
    print(ans - 1)
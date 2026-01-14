# 좌표압축

import sys
input = sys.stdin.readline

num = int(input())
arr = list(map(int, input().split()))
std_arr = sorted(list(set(arr)))
dic_arr = {std_arr[i] : i for i in range(len(std_arr))}

for nums in arr :
    print(dic_arr[nums], end = ' ')
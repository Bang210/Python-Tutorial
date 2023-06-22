import sys
input = sys.stdin.readline
from collections import deque

num_people, cycle = map(int, input().split())
arr = deque([i + 1 for i in range(num_people)])
ans = []

while arr :
    for j in range(cycle - 1) :
        arr.append(arr.popleft())
    ans.append(arr.popleft())

print('<', end='')
for k in range(num_people - 1) :
    print(str(ans[k]) + ', ', end = '')
print(str(ans[-1]) + '>')

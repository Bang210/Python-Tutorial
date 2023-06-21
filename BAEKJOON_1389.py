# 유저의 수와 관계의 수가 주어질 때, 케빈 베이컨의 수가 가장 낮은 유저를 구하는 문제
# 케빈 베이컨의 수: 모든 사람과의 관계에서 몇 단계를 통해 이어져 있는지의 합

import sys
input = sys.stdin.readline
from collections import deque

# input과 필요 데이터 설정

num_users, num_connections = map(int, input().split())
graph = [[0] * (num_users + 1) for _ in range(num_users + 1)]
score = list()

for i in range(num_connections) :
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# bfs를 통해 케빈 베이컨의 수를 구하는 함수 구현

def kevin(user) :
    visit = [0 for _ in range(num_users + 1)]
    que = deque([user])
    distance = [0 for j in range(num_users + 1)]
    visit[user] = 1
    while que :
        start = que.popleft()
        for k in range(1, num_users + 1) :
            if graph[start][k] == 1 and visit[k] == 0 :
                que.append(k)
                visit[k] = 1
                distance[k] = distance[start] + 1
    return(sum(distance))

for l in range(1, num_users + 1) :
    score.append(kevin(l))

print(score.index(min(score)) + 1)

# 정답.
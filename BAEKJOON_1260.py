# 그래프의 정점(node/vertex), 간선(edge), 시작점이 주어졌을 때 DFS와 BFS로 탐색한 결과를 각각 출력하는 문제

import sys
from collections import deque
input = sys.stdin.readline

node, edge, start = map(int, input().split())
graph  = [[0] * (node + 1) for _ in range(node + 1)]

for i in range(edge) :
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visit_dfs = [0 for _ in range(node + 1)]
visit_bfs = visit_dfs.copy()
stack = [start]
que = deque([start])

def dfs(s) :
    visit_dfs[s] = 1
    print(s, end = ' ')
    for i in range(1, node + 1) :
        if graph[s][i] == 1 and visit_dfs[i] == 0 :
            dfs(i)

def bfs(s) :
    visit_bfs[s] = 1
    while que :
        s = que.popleft()
        visit_bfs[s] = 1
        print(s, end = ' ')
        for i in range(1, node + 1) :
            if visit_bfs[i] == 0 and graph[s][i] == 1 :
                que.append(i)
                visit_bfs[i] = 1

dfs(start)
print()
bfs(start)
# 노드와 엣지의 개수, 연결이 주어졌을 때 연결요소의 개수숟

import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

num_nodes, num_edges = map(int, input().split())
components = num_nodes
visit = [0 for _ in range(num_nodes + 1)]
graph = [([0] * (num_nodes + 1)) for _ in range (num_nodes + 1)]
visit[0] = -1

for i in range(num_edges) :
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(s) :
    global components
    visit[s] = 1
    for j in range(1, num_nodes + 1) :
        if visit[j] == 0 and graph[s][j] == 1 :
            components -= 1
            dfs(j)

cnt = 1
while 0 in visit :
    dfs(cnt)
    cnt += 1

print(components)
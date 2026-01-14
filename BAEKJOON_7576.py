import sys
input = sys.stdin.readline

width, length = map(int, input().split())
box = [([2] * (width + 2)) for _ in range(length + 2)]
for i in range(1, length + 1) :

    box[i] = map(int, input().split())
que = list()
date = 0

# for j in range(1, length + 1) :
#     for k in range(1, width + 1) :
#         if box[j][k] == 1 :
#             que.append((j, k,))

# if not que :
#     print(-1)
# else :
#     while que :
#         a, b = que.pop(0)
#         if box[a][b + 1] == 0 :
#             que.append((a, b + 1,))
#         if box[a + 1][b] == 0 :
#             que.append((a + 1, b,))
#         if box[a][b - 1] == 0 :
#             que.append((a, b - 1))
#         if box[a - 1][b] == 0 :
#             que.append((a - 1, b,))

print(box)
# M 과 N이 주어졌을 때, 주어진 M * N 크기의 무작위로 칠해진 판에 대해, 
# 8 * 8 영역을 선택한 후 정상적인 체스판을 만들기 위해 칠해야 하는 칸 수의 최소값을 구하는 문제

ideal_white = ['WBWBWBWB','BWBWBWBW', 
               'WBWBWBWB', 'BWBWBWBW', 
               'WBWBWBWB', 'BWBWBWBW', 
               'WBWBWBWB', 'BWBWBWBW']

height, width = map(int, input().split())
height_remain = height - 7
width_remain = width - 7
least = 64
board = list()

for _ in range(height) :
    board.append(input())

for i in range(height_remain) :
    for j in range(width_remain) :
        count_black = 0
        count_white = 0
        for k in range(8) :
            for l in range(8) :
                if board[k + i][l + j] == ideal_white[k][l]:
                     count_black += 1
                else :
                    count_white += 1
        count = min(count_black, count_white)
        if count < least :
            least = count

print(least)

#정답
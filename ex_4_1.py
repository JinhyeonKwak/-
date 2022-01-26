# 상하좌우

n = int(input())
plans = list(input().split())
move_types = ['L', 'R', 'U', 'D']
x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


for plan in plans:
    for i in range(4):
        if move_types[i] == plan:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx >= 1 and nx <= n and ny >=1 and ny <= n:
        x, y = nx, ny

print(x, y)
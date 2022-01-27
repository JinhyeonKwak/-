from collections import deque

n, m = map(int, input().split())
game_map = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque([(0, 0)])

while queue:
    v = queue.popleft()
    x, y = v[0], v[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx <= n - 1 and ny >= 0 and ny <= m - 1:
            if game_map[nx][ny] == 1:
                game_map[nx][ny] = game_map[x][y] + 1
                queue.append((nx, ny))

result = game_map[n-1][m-1]
print(result)







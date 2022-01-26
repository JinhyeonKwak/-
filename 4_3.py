# 게임 개발

n, m = map(int, input().split())
x, y, d = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(n)]

visited = []
visited.append([x, y])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0
while True:
    d -= 1
    cnt += 1
    if d < 0:
        d = 3
    nx = x + dx[d]
    ny = y + dy[d]
    if nx >= 0 and nx <= m - 1 and ny >= 0 and ny <= m - 1:
        if game_map[nx][ny] == 0 and [nx, ny] not in visited:
            visited.append([nx, ny])
            x, y = nx, ny
            cnt = 0
            continue

    if cnt == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if nx >= 0 and nx <= m - 1 and ny >= 0 and ny <= m - 1:
            if game_map[nx][ny] == 1:
                break
            else:
                x, y = nx, ny
                cnt = 0
        else:
            break

result = len(visited)
print(result)





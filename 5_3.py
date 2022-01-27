# 음료수 얼려 먹기

n, m = map(int, input().split())

ice_frame = []
for i in range(n):
    ice_frame.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def find_empty(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if ice_frame[x][y] == 0:
        ice_frame[x][y] = 1

        # for i in range(4):
        #     nx = x + dx[i]
        #     ny = y + dy[i]
        #     if find_empty(nx, ny):
        #         continue
        find_empty(x-1, y)
        find_empty(x+1, y)
        find_empty(x, y-1)
        find_empty(x, y+1)
        return True
    else:
        return False

# def print_ice(ice_frame):
#     for i in range(n):
#         print(ice_frame[i])
#     print('----------------------')


result = 0
for i in range(n):
    for j in range(m):
        # print_ice(ice_frame)
        if find_empty(i, j):
            result += 1

print(result)

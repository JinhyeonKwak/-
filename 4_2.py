# 왕실의 나이트

pos = input()
x = int(pos[1])
y = int(ord(pos[0])) - int(ord('a')) + 1

# dx = [-2, -1, 1, 2, 2, 1, -1, -2]
# dy = [1, 2, 2, 1, -1, -2, -2, -1]
steps = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

result = 0
for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
         result += 1


# result = 0
# for i in range(len(dx)):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
#         result += 1


print(result)

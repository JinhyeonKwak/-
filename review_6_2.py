# 위에서 아래로

n = int(input())
array = [int(input()) for _ in range(n)]

result = sorted(array, reverse=True)
for x in result:
    print(x, end=' ')


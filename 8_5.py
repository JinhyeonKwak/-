# 효율적인 화폐 구성

n, m = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()

d = [10001] * (m+1)
d[0] = 0
for x in coins:
    for i in range(x, m+1):
        d[i] = min(d[i], d[i-x]+1)

result = d[m]
if result == 10001:
    print(-1)
else:
    print(result)

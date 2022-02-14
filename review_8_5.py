n, m = map(int, input().split())
array = [int(input()) for _ in range(n)]

d = [10001] * (m+1)
d[0] = 0
for x in array:
    for i in range(x, m + 1):
        d[i] = min(d[i], d[i-x]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])





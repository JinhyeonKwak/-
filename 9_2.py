# 미래 도시
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1

x, k = map(int, input().split())

for t in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][t] + graph[t][j])

result = graph[1][k] + graph[k][x]

if result >= INF:
    print(-1)
else:
    print(result)




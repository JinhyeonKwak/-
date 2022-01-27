# BFS 메서드 정의

from collections import deque

def bfs(graph, start, visited):
    visited[start] = True
    deq = deque([start])

    while deq:
        v = deq.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                deq.append(i)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
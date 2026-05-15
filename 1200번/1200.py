import sys

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
def node_sort():
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, N + 1):
        graph[i].sort()

sys.setrecursionlimit(100000)
g_dfs = [False] * (N + 1)
def dfs(n):
    g_dfs[n] = True
    print(n,end = " ")
    for i in graph[n]:
        if not g_dfs[i]:
            dfs(i)


from collections import deque

g_bfs = [False] * (N + 1)
def bfs(n):
    queue = deque([n])
    g_bfs[n] = True
    while queue:
        n = queue.popleft()
        print(n, end=' ')
        for i in graph[n]:
            if not g_bfs[i]:
                queue.append(i)
                g_bfs[i] = True

node_sort()
dfs(1)
print()
bfs(1)
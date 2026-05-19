import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10*6)

farm = []
for i in range(10):
    line = list(input())
    farm.append(line)
    if "B" in line:
        y = i
        x = line.index("B")

farm[y][x] = 0

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(Y,X):
    result = False
    queue = deque([(Y,X)])
    while not result:
        y,x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 10 and 0 <= ny < 10:
                if farm[ny][nx] == ".":
                    farm[ny][nx] = farm[y][x] + 1
                    queue.append((ny, nx))
                elif farm[ny][nx] == "L":
                    print(farm[y][x])
                    result = True

bfs(y,x)
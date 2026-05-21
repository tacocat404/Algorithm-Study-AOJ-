import sys
input = sys.stdin.readline
from collections import deque
import heapq
Y,X = map(int,input().split())

farm = []
visited = [[False for _ in range(X)] for _ in range(Y)]
for _ in range(Y):
    farm.append(list(map(int,input().split())))

K = int(input())

dy = [0,0,-1,1]
dx = [-1,1,0,0]

def start_setting(visited):
    visited[0] = [True for _ in range(X)]
    visited[Y - 1] = [True for _ in range(X)]
    for i in range(Y):
        visited[i][0] = True
        visited[i][X - 1] = True


vist = []

for i in range(X):
    if 0 != Y - 1:
        heapq.heappush(vist,(-farm[0][i],0,i))
        heapq.heappush(vist,(-farm[Y-1][i],Y-1,i))
    else:
        heapq.heappush(vist,(-farm[0][i],0,i))
for j in range(1,Y - 1):
    if 0 != X - 1:
        heapq.heappush(vist,(-farm[j][0],j,0))
        heapq.heappush(vist,(-farm[j][X-1],j,X-1))
    else:
        heapq.heappush(vist,(-farm[j][0],j,0))

start_setting(visited)

def wasd():
    v,y,x = heapq.heappop(vist)
    print(f"{y + 1} {x + 1}")
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < X and 0 <= ny < Y and not visited[ny][nx]:
            heapq.heappush(vist,(-farm[ny][nx],ny,nx))
            visited[ny][nx] = True

# for _ in range(K):
#     max_value = 0
#     for i in vist:
#         y,x = i
#         if max_value < farm[y][x]:
#             max_value = farm[y][x]
#             ly,lx = y,x
#     wasd(ly,lx)

for _ in range(K):
    wasd()
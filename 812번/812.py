import sys
import copy
input = sys.stdin.readline
Y,X = int(input())
maze = []
for _ in range(Y):
    maze.append(list(map(int,input())))
copied_list = [row[:] for row in original_list]
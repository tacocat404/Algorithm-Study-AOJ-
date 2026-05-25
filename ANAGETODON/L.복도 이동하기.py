import sys
input = sys.stdin.readline
N,M = map(int,input().split())
Y = 1
X = 1
count = 0
numbers = []
for _ in range(M):
    y,x = map(int,input().split())
    numbers.append((y,x))

numbers = sorted(numbers,key =lambda x: x[1])
for y,x in numbers:
    if y == 1 and Y == 1:
        count += 1
        Y = 2
    elif y == 2 and Y == 2:
        count += 1
        Y = 1

if count == 0:
    print(N)
elif Y == 1:
    print(N + count )
else:
    print(N + count - 1)
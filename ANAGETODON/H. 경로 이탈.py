N = int(input())
numbers = []
for i in range(N):
    x,y = map(int,input())
    numbers.append((x,y))

x = 0
y = 0
for i in numbers:
    X,Y = i
    if X >= x:
        X = x
        maxx = (X,Y)
    if Y >= y:
        Y = y
        maxx = (X,Y)

for i in numbers:
    if X >= x:
        X = x
        minx = (X,Y)
    if Y >= y:
        Y = y
        miny = (X,Y)


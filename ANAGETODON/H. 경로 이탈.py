N = int(input())
link = list(input().split("/"))
link = link[1:]
current = ""
for i in link:
    if i == "..":
        current = ""
        break
    elif i == ".":
        current = ""
    else:
        current = i
print("/" + current)
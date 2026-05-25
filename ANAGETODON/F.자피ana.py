A = input()
B = input()
C = ""
S = len(A)

ans = False
for i in range(S):
    C = A[S - 1 - i:] + A[0:S - 1 - i]
    if C == B:
        ans = True
if ans:
    print("PIZZA!")
else:
    print("ZZAPI?")
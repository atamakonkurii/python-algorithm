d = int(input())
n = int(input())

LR = [list(map(int,input().split())) for _ in range(n)]

B = [0] * d
C = [0]

for i in range(n):
    l, r = LR[i]
    B[l-1] += 1
    B[r] -= 1

for i in range(d):
    sum = C[-1] + B[i]
    C.append(sum)

for c in C[1:]:
    print(c)

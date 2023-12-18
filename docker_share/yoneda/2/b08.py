N = int(input())

X = [0] * N
Y = [0] * N

for i in range(N):
    X[i], Y[i] = map(int, input().split())

Q = int(input())

a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q

for i in range(Q):
    a[i], b[i], c[i], d[i] = map(int, input().split())


Z = [ [ 0 ] * 1501 for i in range(1501) ]

for i in range(N):
    Z[X[i]][Y[i]] += 1

# 横
for i in range(1, 1501):
    for j in range(1, 1501):
        Z[i][j] =  Z[i][j-1] + Z[i][j]

# 縦
for j in range(1, 1501):
    for i in range(1, 1501):
        Z[i][j] =  Z[i-1][j] + Z[i][j]

for i in range(Q):
    answer = Z[c[i]][d[i]] -  Z[c[i]][b[i]-1] -  Z[a[i]-1][d[i]] + Z[a[i]-1][b[i]-1]
    print(answer)
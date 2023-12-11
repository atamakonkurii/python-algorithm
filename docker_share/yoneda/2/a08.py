H, W = map(int, input().split())

# X = [[0]* W] * H
X = [[0 for i in range(W)] for j in range(H)]
for i in range(W):
    X[i] = list(map(int, input().split()))

Q = int(input())

A = [ 0 ] * Q
B = [ 0 ] * Q
C = [ 0 ] * Q
D = [ 0 ] * Q

for k in range(Q):
    A[k], B[k], C[k], D[k] = map(int, input().split())


Z = [[0 for i in range(W)] for j in range(H)]

# 横
for h1 in range(H):
    Z[h1][0] = X[h1][0]
    for w1 in range(1, W):
        Z[h1][w1] = Z[h1][w1 - 1] + X[h1][w1]

# 縦
for w2 in range(W):
    for h2 in range(1, H):
        Z[h2][w2] = Z[h2-1][w2] + Z[h2][w2]

print(Z)

for q in range(Q):
    # print(q,C[q],D[q])
    answer = Z[C[q]-1][D[q]-1] - Z[C[q]-1][B[q-1]-1] - Z[A[q-1]-1][D[q]-1] + Z[A[q-1]-1][B[q-1]-1]
    print(Z[C[q]-1][D[q]-1] , Z[C[q]-1][B[q-1]-1] , Z[A[q-1]-1][D[q]-1] , Z[A[q-1]-1][B[q-1]-1])
    print(answer)
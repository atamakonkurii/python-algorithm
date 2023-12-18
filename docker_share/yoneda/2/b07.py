T = int(input())
N = int(input())
L = [ None ] * N
R = [ None ] * N
for i in range(N):
    L[i], R[i] = map(int, input().split())

CL = [0] * (T + 1)
for i in range(N):
    CL[L[i]] += 1
    CL[R[i]] -= 1

SL = [ None ] * (T + 1)
SL[0] = CL[0]
for k in range(1, T+1):
    SL[k] = SL[k -1] + CL[k]

for j in range(T):
    print(SL[j])
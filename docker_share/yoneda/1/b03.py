n = int(input())
A = list(map(int, input().split()))

for i in range(n-2):
    for j in range(i + 1, n-1):
        for k in range(j + 1, n):
            if A[i] + A[j] + A[k] == 1000:
                print('Yes')
                exit()
print('No')
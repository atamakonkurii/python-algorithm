n, k = map(int, input().split())

count = 0

max_r = min(k-1, n+1)

for r in range(1, max_r):
    for g in range(1, max_r):

        x = k - r - g

        if x >= 1 and x <= n:
            count += 1

print(count)
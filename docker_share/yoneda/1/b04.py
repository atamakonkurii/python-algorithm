n = int(input())

ans = 0
for i in range(7 ,-1, -1):
    q, r = divmod(n, (10 ** i))

    if q == 1:
        ans += 2 ** i

    n = r

print(ans)
n, q = map(int, input().split())
A = list(map(int, input().split()))
L = [list(map(int, input().split())) for _ in range(q)]

waList = [0]

for a in A:
    wa = a + waList[-1]
    waList.append(wa)

for (l, q) in L:
    print(waList[q] - waList[l-1])

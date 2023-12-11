n = int(input())
A = list(map(int, input().split()))
q = int(input())
L = [list(map(int, input().split())) for _ in range(q)]

Atari = [0]
Hazure = [0]

for a in A:
    if a == 1:
        atari_wa = Atari[-1] + 1
        hazure_wa = Hazure[-1] + 0
        Atari.append(atari_wa)
        Hazure.append(hazure_wa)
    else:
        atari_wa = Atari[-1] + 0
        hazure_wa = Hazure[-1] + 1
        Atari.append(atari_wa)
        Hazure.append(hazure_wa)


for (l, r) in L:
    atari_diff = Atari[r] - Atari[l-1]
    hazure_diff = Hazure[r] - Hazure[l-1]

    diff = atari_diff - hazure_diff

    if diff == 0:
        print("draw")
    elif diff > 0:
        print("win")
    else:
        print("lose")

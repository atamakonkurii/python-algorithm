n = int(input())

text = ''
for i in range(9, -1, -1):
    q, r = divmod(n, (2 ** i))

    if q == 1:
        text += '1'
    else:
        text += '0'

    n = r

print(text) 
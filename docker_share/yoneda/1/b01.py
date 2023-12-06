import sys

min, max = map(int, input().split())

for num in range(min, max + 1):
  if (100 % num) == 0:
    print('Yes')
    sys.exit()
    
print('No')
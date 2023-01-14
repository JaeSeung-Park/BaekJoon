import sys
n = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))
p = list(map(int, sys.stdin.readline().split()))
total = 0
c = p[0]
for i in range(len(k)):
    if c > p[i]:
        c = p[i]
    total += c * k[i]    
    
print(total)
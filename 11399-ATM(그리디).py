import sys
n = int(sys.stdin.readline())
sum = 0
a = list(map(int, sys.stdin.readline().split()))
a.sort()
for i in range(n):
    sum += (n - i) * a[i]
    
print(sum)
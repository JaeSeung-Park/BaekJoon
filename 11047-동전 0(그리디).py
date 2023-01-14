import sys
n, k = map(int, sys.stdin.readline().split())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))
    
count = 0
for i in range(n):
    if k == 0:
        break
    if a[n - i - 1] <= k:
        count = count + k // a[n - i - 1]
        k = k % a[n - i - 1]
            
print(count)
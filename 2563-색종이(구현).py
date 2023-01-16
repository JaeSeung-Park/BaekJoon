import sys
n = int(sys.stdin.readline())
a = [[0] * 100 for _ in range(100)]
r = 0
for _ in range(n):
    m, n = map(int, sys.stdin.readline().split())
    for i in range(10):
        for j in range(10):
            a[m + i][n + j] = 1
            
for i in a:
    r += sum(i)
print(r)
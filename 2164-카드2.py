import sys
n = int(sys.stdin.readline())
m = 1
while True:
    m *= 2
    if (n == 1 or n == 2):
        print(n)
        break
    if (n <= m):
        print((n - (m // 2)) * 2)
        break

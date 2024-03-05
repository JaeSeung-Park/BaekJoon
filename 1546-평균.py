import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
print(sum(a) / max(a) * 100 / n)
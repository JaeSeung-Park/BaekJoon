import sys
k = int(sys.stdin.readline())
for _ in range(k):
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    index = [0 for i in range(n)]
    index[m] = 1
    c = 0
    
    while a:
        if a[0] == max(a):
            c += 1
            if index[0] == 1:
                print(c)
                break
            a.pop(0)
            index.pop(0)
        else:
            a.append(a.pop(0))
            index.append(index.pop(0))
import sys
k = int(sys.stdin.readline())
a = []
sum = 0
for i in range(k):
    n = int(sys.stdin.readline())
    if n != 0:
        a.append(n)
    else:
        a.pop()
        
for i in a:
    sum += i
    
print(sum)
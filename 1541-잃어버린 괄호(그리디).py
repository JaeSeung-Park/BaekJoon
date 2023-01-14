import sys
s = sys.stdin.readline().split('-')
num = []
for i in s:
    n = 0
    k = i.split('+')
    for j in k:
        n += int(j)
    num.append(n)
sum = 0
for i in range(len(num)):
    sum -= num[i]
sum += 2 * num[0]
print(sum)
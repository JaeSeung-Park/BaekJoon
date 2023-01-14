n = int(input())
a = []
for _ in range(n):
    a.append(input())

a.sort(reverse=False)
a.sort(key=len, reverse=False)
r = list(dict.fromkeys(a))
for i in range(len(r)):
    print(r[i])
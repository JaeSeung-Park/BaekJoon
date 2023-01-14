def hanoic(n, f, t, a):
    if n == 1:
        print(f, t)
        return
    hanoic(n-1, f, a, t)
    print(f, t)
    hanoic(n-1, a, t, f)

def hanoi(n, f, t, a):
    if n == 1:
        return 1
    c = 0
    c = c + hanoi(n-1, f, a, t)
    c = c + 1
    c = c + hanoi(n-1, a, t, f)
    return c

n = int(input())
print(hanoi(n, 1, 3, 2))
hanoic(n, 1, 3, 2)
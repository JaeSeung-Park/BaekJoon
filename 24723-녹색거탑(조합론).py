n = int(input())
def down(a):
    if a == 1:
        return 1
    else:
        return 2 * down(a - 1)
print(2 * down(n))
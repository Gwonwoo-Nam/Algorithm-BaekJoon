import sys

n = int(input())
val = []

for i in range(n):
    val.append(list(map(int, sys.stdin.readline().rstrip().split())))

def divide(n, val, r, c):
    global w, b
    if n == 1 and val[r][c] == 1:
        w += 1
        return
    if n == 1 and val[r][c] == 0:
        b += 1
        return
    count = countFilled(n, val, r, c)
    if count == n * n:
        w += 1
        return
    elif count == 0:
        b += 1
        return
    else:
        h = int(n / 2)
        divide(h, val, r, c)
        divide(h, val, r + h, c)
        divide(h, val, r, c + h)
        divide(h, val, r + h, c + h)


def countFilled(n, val, r, c):
    count = 0
    for row in range(r, r + n):
        for col in range(c, c + n):
            if val[row][col]:
                count += 1
    return count


w = 0
b = 0

divide(n, val, 0, 0)
print(b)
print(w)

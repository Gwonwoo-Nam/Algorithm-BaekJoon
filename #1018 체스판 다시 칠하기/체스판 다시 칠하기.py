import sys

n, m = map(int, sys.stdin.readline().split())

arr = []

for i in range(n) :
    arr += sys.stdin.readline().split()

blacksum = 0
whitesum = 0
ans = 217372931
for k in range(0, n-7) :
    for r in range(0, m-7) :
        for i in range(8) :
            for j in range(8) :
                index = ((k + i) % 2 + (j + r) % 2) % 2
                if index == 0 :
                    index = "B"
                else :
                    index = "W"
                if arr[k+i][(j + r)] == index :
                    blacksum += 1
        ans = min(ans, blacksum)
        blacksum = 0

for k in range(0, n-7) :
    for r in range(0, m-7) :
        for i in range(8) :
            for j in range(8) :
                index = ((k + i) % 2 + (j + r) % 2 + 1) % 2
                if index == 0 :
                    index = "B"
                else :
                    index = "W"
                if arr[k+i][(j + r)] == index :
                    whitesum += 1
        ans = min(ans, whitesum)
        whitesum = 0

print(ans)

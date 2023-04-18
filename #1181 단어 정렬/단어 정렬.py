import sys

n = int(sys.stdin.readline()[:-1])
arr = []
rep = []


def compare(str) :
    return (len(str), str)

for i in range (n) :
    arr +=sys.stdin.readline().split()

for item in arr :
    if item not in rep :
        rep.append(item)

rep.sort(key=lambda x: compare(x))

for item in rep :
    print(item)


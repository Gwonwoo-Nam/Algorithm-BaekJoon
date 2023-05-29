import sys

k, n = map(int, input().split())

cables = []
for i in range (k) :
    cables.append(int(sys.stdin.readline().rstrip()))
low = 1
high = int(2e31)
def binarySearch() :
    global low
    global high
    count = 0
    while (low + 1 < high) :
        mid = int((high + low) / 2)
        count = 0
        for cable in cables :
            count += int(cable / mid)
        if count < n :
            high = mid
        else :
            low = mid


binarySearch()
print (low)

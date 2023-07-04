import sys

n,m = map(int, input().split())

numbers = list(map(int,input().split()))
partialSum = []

partialSum.append(numbers[0])
for i in range(1,n) :
    partialSum.append(partialSum[i-1] + numbers[i])

for i in range(m) :
    i,j = map(int,sys.stdin.readline().rstrip().split())
    if i-2 >= 0 :
        print(partialSum[j-1] - partialSum[i-1-1])
    else :
        print(partialSum[j-1])

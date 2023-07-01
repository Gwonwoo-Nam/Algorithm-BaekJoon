import sys

n = int(input())
arr = [0 for i in range(10001)]

for i in range (n) :
  arr[int(sys.stdin.readline().rstrip()) - 1] += 1

# print(arr)
# countSum = [0 for i in range(n+1)]
# countSum[0] = arr[0]
# for i in range (1, len(arr)) :
#   countSum[i] = countSum[i-1] + arr[i]

index = 0
for i in arr :
  index += 1
  for j in range (i) :
    print(index)
import sys

n,m = map(int,input().split())

chicken = []
house = []

for r in range(n) :
  c = 0
  for num in map(int, sys.stdin.readline().rstrip().split()) :
    if num == 1 :
      house.append((r,c))
    elif num == 2 :
      chicken.append((r,c))
    c+=1

mi = 10000000

def dfs(k, last, house, arrive) :
  global mi
  global m
  if k == m :
    mi = min(mi, getDistance(house, arrive))
    # print(arrive)
    return
  for i in range(last, len(chicken)) :
    arrive.append(chicken[i])
    dfs(k + 1, i+1, house, arrive)
    arrive.pop()

def getDistance(house, arrive) :
  sum = 0
  for h in house :
    dis = 10000000
    for c in arrive :
      dis = min(dis, abs(c[0] - h[0]) + abs(c[1] - h[1]))
    sum += dis
  return sum

arrive = []

dfs(0, 0, house, arrive)
print(mi)
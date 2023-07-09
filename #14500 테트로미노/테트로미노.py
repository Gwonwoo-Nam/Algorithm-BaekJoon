from collections import deque
n,m = map(int, input().split())

arr = []
for i in range(n) :
  arr.append(list(map(int,input().split())))
q = deque()

move = [[1,0],[0,1], [-1,0],[0,-1]]

moveslist = []
for i in move :
  for j in move :
    for k in move :
      a = [a+b+c for a,b,c in zip(i,j,k)]
      if abs(a[0])+abs(a[1]) == 3 :
        moveslist.append(list(([0,0],i,j,k)))

mlist = []
mlist.append(list(([0,0],[1,0],[0,1],[0,-1])))
mlist.append(list(([0,0],[-1,0],[0,1],[0,-1])))
mlist.append(list(([0,0],[1,0],[-1,0],[0,-1])))
mlist.append(list(([0,0],[1,0],[-1,0],[0,1])))
mlist.append(list(([0,0],[1,0],[0,1],[1,1])))
mlist.append(list(([0,0],[1,0],[0,-1],[1,-1])))
mlist.append(list(([0,0],[-1,0],[0,1],[-1,1])))
mlist.append(list(([0,0],[-1,0],[0,-1],[-1,-1])))
maxSum = 0
for i in range(n) :
  for j in range(m) :
    for moves in moveslist :
      sum = 0
      flag = True
      r = i
      c = j
      for dx,dy in moves :
        if r+dx >= 0 and r+dx < n and c+dy >= 0 and c+dy < m :
          sum += arr[r+dx][c+dy]
          r = r+dx
          c = c+dy
        else :
          flag = False
          break
      if flag == True :
        maxSum = max(sum, maxSum)

for i in range(n) :
  for j in range(m) :
    for moves in mlist :
      sum = 0
      flag = True
      r = i
      c = j
      for dx,dy in moves :
        if r+dx >= 0 and r+dx < n and c+dy >= 0 and c+dy < m :
          sum += arr[r+dx][c+dy]
        else :
          flag = False
          break
      if flag == True :
        maxSum = max(sum, maxSum)

print(maxSum)

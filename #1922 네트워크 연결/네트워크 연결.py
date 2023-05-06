import sys


def union(li, con) :
  # 부모 노드 설정
  a = findParent(li[0], con)
  b = findParent(li[1], con)

  if (a < b):
    con[b - 1][1] = a
  else :
    con[a - 1][1] = b

def findParent(x, con) :
  if con[x-1][1] != x :
    return findParent(con[x-1][1], con)
  return x

def isOK(li, con) :
  return findParent(li[0],con) == findParent(li[1],con)

n = int(input());
m = int(input());

li = []
for i in range(m) :
  li.append(list(map(int,sys.stdin.readline().rstrip().split(" "))))

li.sort(key=lambda x: x[2])

con = [[i, i] for i in range(1,n+1)]

answer = 0
for i in range (len(li)):
  # 사이클이 발생하지 않는 경우
  if isOK(li[i], con) == False :
    #for j in range(i+1):
    union(li[i], con)
    answer += li[i][2]


# 
# print(con)
# print(li)
print(answer)
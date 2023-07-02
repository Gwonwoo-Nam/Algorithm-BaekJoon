from collections import deque

n,k = map(int, input().split())

q = deque()
for i in range(1,n+1) :
  q.append(i)

i = k
answer = []
while len(q) > 0 :
  i -= 1
  a = q.popleft()
  if i == 0 :
    i = k
    answer.append(a)
  else :
    q.append(a)


print("<"+ ", ".join(map(str,answer)) + ">")
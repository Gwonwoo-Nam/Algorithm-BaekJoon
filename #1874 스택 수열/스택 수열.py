from collections import deque

q = deque()
n = int(input())
res = deque()

for i in range(n):
  res.append(int(input()))

answer = []

for i in range(1, n + 1):
  q.appendleft(i)
  answer.append("+")
  tmp = i
  while len(res) > 0 and len(q) > 0 and res[0] == q[0] :
    answer.append("-")
    q.popleft()
    res.popleft()



if len(res) > 0:
  print("NO")
else :
  print("\n".join(answer))
from collections import deque
import sys
k = int(input())

q = deque()
for i in range(k) :
  num = int(sys.stdin.readline().rstrip())
  if num == 0 and len(q) > 0 :
    q.popleft()
  else :
    q.appendleft(num)
print(sum(q))
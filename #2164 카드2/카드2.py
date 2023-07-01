from collections import deque

n = int(input())
queue = deque()

for i in range(1, n+1) :
  queue.append(i)


for i in range(1, n) :
  queue.popleft()
  a = queue.popleft()
  queue.append(a)

print(queue.popleft())
from collections import deque

def peek(queue) :
  if len(queue) > 0 :
    a = queue.popleft()
    queue.appendleft(a)
    return a

n = int(input())


for i in range(n) :
  str = input()
  queue = deque()
  for j in list(str):
    if len(queue) == 0 :
      queue.appendleft(j)
    elif len(queue) > 0 and peek(queue) == "(" and j == ")" :
      queue.popleft()
    else :
      queue.appendleft(j)
  if len(queue) > 0 :
    print("NO")
  else :
    print("YES")


def check(queue) :
  while len(queue) > 0 :
    a = queue.popleft()
    if queue.size() > 0 and a == "(" and peek(queue) == ")" :
      queue.popleft()

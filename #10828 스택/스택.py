from collections import deque
import sys

def run(deq) :
  inputs = sys.stdin.readline().rstrip()
  if inputs == "top" :
    if len(deq) == 0 :
      return -1
    return deq[0]
  elif inputs == "size" :
    return len(deq)
  elif inputs == "empty" :
    if len(deq) == 0 :
      return 1
    return 0
  elif inputs == "pop" :
    if len(deq) == 0 :
      return -1
    return deq.popleft()
  else :
    a = int(inputs.split()[1])
    deq.appendleft(a)


n = int(input())

deq = deque()
for i in range(n) :
  result = run(deq)
  if result is not None :
    print(result)


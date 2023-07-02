from collections import deque

def balance(str, q) :
  for i in str :
    if i == "[" :
      q.appendleft(i)
    elif i == "]" :
      if len(q) > 0 and q[0] == "[" :
        q.popleft()
      else :
        print("no")
        return
    if i == "(" :
      q.appendleft(i)
    elif i == ")" :
      if len(q) > 0 and q[0] == "(" :
        q.popleft()
      else :
        print("no")
        return
  if len(q) == 0 :
    print("yes")
  else :
    print("no")

while True :
  str = input()
  q = deque()
  if str == "." :
    break
  balance(str, q)


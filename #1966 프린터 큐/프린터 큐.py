from collections import deque
testcases = int(input())

def check(q, a) :
  for i in q :
    if i[0] > a[0] :
      q.append(a)
      return True
  return False

for i in range(testcases):
  n, m = map(int, input().split())
  li = list(map(int, input().split()))
  q= deque()
  index = 0
  for j in li :
    q.append((j, index==m))
    index += 1

  count = 0
  while len(q) > 0 :
    a = q.popleft()

    if check(q, a) == False :
      count += 1
      if a[1] == True :
        print(count)



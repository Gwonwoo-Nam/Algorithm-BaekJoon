import sys
def new_round(num):
  if num - int(num) >= 0.5:
    return int(num) + 1
  else:
    return int(num)

n = int(input())


li = []
if n == 0 :
  print(0)
else :
  for i in range(n) :
    li.append(int(sys.stdin.readline().rstrip()))
  li.sort()
  m = new_round(n*0.15)
  ans = li[m:n-m:1]
  sum = new_round(sum(ans)/len(ans))
  print(sum)


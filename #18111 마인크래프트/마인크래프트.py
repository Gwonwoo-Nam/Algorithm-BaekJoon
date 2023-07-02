import sys
n, m, b = map(int,input().split())

li = []
for i in range(n) :
  li += list(map(int,sys.stdin.readline().rstrip().split()))

min_h = min(li)
max_h = max(li)
result_sec = 99999999
result_h = 0


for i in range(min_h, max_h+1) :
  count = 0
  tmp = b
  for item in li :
    diff = i - item
    if diff > 0 :
      tmp -= diff
      count += diff
    elif diff < 0 :
      count -= 2 * diff
      tmp -= diff
  if tmp >= 0 :
    if result_sec >= count :
      result_sec = count
      result_h = i


print(result_sec, result_h)
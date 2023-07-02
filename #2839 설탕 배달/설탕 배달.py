n = int(input())
count = 0
if n % 5 == 0 :
  print(int(n/5))
else :
  while n > 0 and n % 5 != 0 :
    n -= 3
    count += 1
  if n < 0 :
    print(-1)
  else :
    print(int(count+n/5))
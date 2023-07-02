import math
m,n = map(int, input().split())


def isPrime(number):
  if number == 1 :
    return False
  if number == 2 :
    return True
  for i in range(2, math.floor(math.sqrt(number))+2) :
    if number % i == 0 :
      return False
  return True

for i in range(m, n+1) :
  if isPrime(i) :
    print(i)

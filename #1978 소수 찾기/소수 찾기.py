import math

def isPrime(number):
  if number == 1 :
    return False
  if number == 2 :
    return True
  for i in range(2, math.floor(math.sqrt(number))+2) :
    if number % i == 0 :
      return False
  return True

n = int(input())
numbers = list(map(int, input().split()))
count = 0
for i in numbers :
  if isPrime(i) :
    count += 1
print(count)
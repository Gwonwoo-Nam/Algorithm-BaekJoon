n = int(input())

countTwo = 0
countFive = 0

for i in range(1, n+1) :
  while i%2 == 0 :
    countTwo += 1
    i /= 2
  while i%5 == 0 :
    countFive += 1
    i /= 5

print(min(countTwo, countFive))
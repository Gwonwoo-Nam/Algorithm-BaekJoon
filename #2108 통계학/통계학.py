from collections import defaultdict
import sys
import math

def arithmeticMean(numbers) :
  sum = 0
  for i in numbers :
    sum += i
  return int(round(sum/len(numbers),0))

def median(numbers) :
  numbers.sort()
  return numbers[int(len(numbers)/2)]

def frequency(numbers) :
  map = defaultdict(int)
  for number in numbers :
    map[number] += 1

  iter = [(value, key) for key, value in map.items()]

  iter.sort(key=lambda x: (x[0], -x[1]))
  
  if len(iter) > 1 and iter[-1][0] == iter[-2][0] :
    return iter[-2][1]
  else :
    return iter[-1][1]


def ran(numbers) :
  return max(numbers) - min(numbers)

n = int(input())

li = []
for i in range(n) :
  li.append(int(sys.stdin.readline().rstrip()))

print(arithmeticMean(li))
print(median(li))
print(frequency(li))
print(ran(li))

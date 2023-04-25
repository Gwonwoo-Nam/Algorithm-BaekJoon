import datetime
import sys
s,e,q = sys.stdin.readline().split(" ")

hour, minute = map(int, s.split(":"))
s = datetime.time(hour, minute)
hour, minute = map(int, e.split(":"))
e = datetime.time(hour, minute)
hour, minute = map(int, q.split(":"))
q = datetime.time(hour, minute)

checker = dict()

str = ""
while True :
  try:
    str = sys.stdin.readline()
    hour, minute = map(int, str.split(" ")[0].split(":"))
    t = datetime.time(hour, minute)
    if checker.get(str.split(" ")[1]) == None and (t <= s) :
      checker[str.split(" ")[1]] = 1
    if checker.get(str.split(" ")[1]) == 1 and (t >= e and t <= q) :
      checker[str.split(" ")[1]] = 2
  except:
    break

sum = 0
for item in checker.items() :
  if item[1] == 2 :
    sum += 1

print(sum)




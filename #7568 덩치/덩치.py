n = int(input())


li = []
for i in range(n) :
  x,y = map(int, input().split())
  li.append((x,y))

ans = []
for item in li :
  rank = 1
  for comp in li :
    if comp[0] > item[0] and comp[1] > item[1] :
      rank += 1
  ans.append(rank)
print(" ".join(map(str, ans)))

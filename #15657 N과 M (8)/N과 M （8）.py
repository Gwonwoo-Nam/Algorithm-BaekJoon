n,m = map(int, input().split())
numlist = list(map(int, input().split()))


result = set()
def dfs(arr) :
  if len(arr) == m :
    result.add(tuple(arr))
    return

  c = 1
  if len(arr) != 0 :
    c = max(arr)

  for i in numlist :
    if i >= c :
      arr.append(i)
      dfs(arr)
      arr.remove(i)

dfs([])

li = list(result)
li.sort()
for e in li :
  print(str(e).rstrip(")").lstrip("(").replace(",", ""))

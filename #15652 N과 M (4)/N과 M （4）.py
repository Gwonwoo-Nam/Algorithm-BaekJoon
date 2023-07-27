n,m = map(int, input().split())

result = set()
def dfs(arr) :
  if len(arr) == m :
    result.add(tuple(arr))
    return
  if len(arr) == 0 :
    c = 1
  else :
    c = max(arr)
  for i in range(c, n+1) :
    arr.append(i)
    dfs(arr)
    arr.remove(i)

dfs([])

li = list(result)
li.sort()
for e in li :
  print(str(e).rstrip(")").lstrip("(").replace(",", ""))

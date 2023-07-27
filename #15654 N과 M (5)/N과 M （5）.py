n,m = map(int, input().split())
numlist = list(map(int, input().split()))


result = set()
def dfs(arr) :
  if len(arr) == m :
    result.add(tuple(arr))
    return

  for i in numlist :
    if i not in arr :
      arr.append(i)
      dfs(arr)
      arr.remove(i)

dfs([])

li = list(result)
li.sort()
for e in li :
  print(str(e).rstrip(")").lstrip("(").replace(",", ""))

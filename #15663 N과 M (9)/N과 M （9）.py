from collections import defaultdict

nummap = defaultdict(int)
n,m = map(int, input().split())
numlist = list(map(int, input().split()))
visited = [0 for i in range(len(numlist))]

result = set()
def dfs(arr, visited) :
  if len(arr) == m :
    result.add(tuple(arr))
    return

  for i in range(len(numlist)) :
    if visited[i] == 0 :
      visited[i] = 1
      arr.append(numlist[i])      
      dfs(arr, visited)
      arr.pop()
      visited[i] = 0

dfs([], visited)

li = list(result)
li.sort()

for e in li :
  print(str(e).rstrip(")").lstrip("(").replace(",", ""))


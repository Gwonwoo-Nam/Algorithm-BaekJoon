from collections import defaultdict, deque
n, m = map(int, input().split())

ladder = defaultdict(int)
snake = defaultdict(int)
for i in range(n) :
  lk, lv = map(int, input().split())
  ladder[lk] = lv

for i in range(m) :
  lk, lv = map(int, input().split())
  snake[lk] = lv

q = deque()

move = [1,2,3,4,5,6]
visited = [0 for i in range(101)]
q.append((1,0))
# print(ladder, snake)
while q:
  pos,count = q.popleft()
  # print(pos,count)
  if pos == 100 :
    print(count)

  for m in move :
    if pos+m <= 100 and visited[pos+m] == 0 :

      if pos+m in ladder.keys() and visited[pos+m] == 0 :
        visited[pos+m] = 1
        q.append((ladder[pos+m], count+1))
      elif pos+m in snake.keys() and visited[pos+m] == 0 :
        visited[pos+m] = 1
        q.append((snake[pos+m], count+1))
      else :
        visited[pos+m] = 1
        q.append((pos+m,count+1))



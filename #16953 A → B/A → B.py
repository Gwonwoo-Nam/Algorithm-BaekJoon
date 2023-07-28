from collections import deque

a, b = map(int, input().split())
q = deque()
q.append((a, 1))

ans = -1
while q:
    tmp, count = q.popleft()
    if tmp == b:
        ans = count
        break
    if tmp * 2 <= b:
        q.append((tmp * 2, count + 1))
    if tmp * 10 + 1 <= b:
        q.append((tmp * 10 + 1, count + 1))

print(ans)
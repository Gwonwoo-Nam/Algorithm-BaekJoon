from collections import defaultdict
t = int(input())

for i in range(t) :
    n = int(input())
    li = defaultdict(int)
    s = set()
    for j in range(n) :
        name, type = input().split()
        s.add(name)
        if name not in set() :
            li[type] += 1
    ans = 1
    for k in li.keys() :
        ans *= li[k] + 1
    print(ans - 1)



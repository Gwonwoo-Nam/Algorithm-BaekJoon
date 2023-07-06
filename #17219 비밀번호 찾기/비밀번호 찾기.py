
import sys

n, m = map(int, input().split())

dic = {}
for i in range(n) :
    site, pw = sys.stdin.readline().rstrip().split()
    dic[site] = pw
for j in range(m) :
    s = sys.stdin.readline().rstrip()
    if dic.get(s) :
        print(dic[s])

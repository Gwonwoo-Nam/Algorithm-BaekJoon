import sys

n, m = map(int,input().split())

po = dict()
for i in range(1,n+1) :
    name = sys.stdin.readline().rstrip()
    po[i] = name
    po[name] = i

for i in range(m) :
    inputs = sys.stdin.readline().rstrip()


    if inputs.isdigit() :
        print(po[int(inputs)])
    else :
        print(po[inputs])



import sys

t = int(sys.stdin.readline().rstrip())

def lcm(a,b) :
    return a*b/gcd(a,b)
def gcd(a,b) :
    if b == 0 :
        return a
    return gcd(b, a%b)

def run(m,n,x,y) :
    maxVal = lcm(m,n)
    a = x
    b = x % n
    count = x
    if x == m :
        x = 0
    if y == n :
        y = 0
    while count <= maxVal :
        if b == y :
            return count
        b = (b + m) % n
        count += m
    return -1

for i in range(t) :
    m,n,x,y = map(int, sys.stdin.readline().rstrip().split())
    print(run(m,n,x,y))




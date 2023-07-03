n,r,c = map(int,input().split())

def recur(n,r,c) :
    mid = int(pow(2,n))/2
    if n == 0 :
        return 1
    if r >=mid  and c >= mid :
        return 3*int(pow(2,2*(n-1))) + recur(n-1,r - mid,c - mid)
    elif r >=mid and c < mid :
        return 2*int(pow(2,2*(n-1))) + recur(n-1,r - mid,c)
    elif r < mid and c >= mid :
        return int(pow(2,2*(n-1))) + recur(n-1,r, c-mid)
    else :
        return recur(n-1,r,c)

print(recur(n,r,c) - 1)

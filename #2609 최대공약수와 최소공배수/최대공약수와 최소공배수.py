def gcd(a, b) :
  gcd = 1
  for i in range(1, int(max(a,b))+1):
    if a % i == 0 and b % i == 0 :
      gcd = i
  return gcd

def lcm(a,b) :
  return int((a/gcd(a,b)) * (b/gcd(a,b)) * gcd(a,b))

a, b = map(int,input().split())
print(gcd(a,b))
print(lcm(a,b))
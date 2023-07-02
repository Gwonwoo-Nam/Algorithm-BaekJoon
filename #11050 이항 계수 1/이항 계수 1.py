n,k = map(int,input().split())

def factorial (a) :
  if a <= 1 : return 1
  return a*factorial(a-1)
print(int(factorial(n)/(factorial(k)*factorial(n-k))))


import sys

while True :
    input = sys.stdin.readline()[:-1]
    if int(input) == 0 :
        break
    if input == input[::-1] :
        print("yes")
    else :
        print("no")


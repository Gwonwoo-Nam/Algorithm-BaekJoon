from collections import deque

def process() :
    global reverse
    for f in func :
        if f == "R" :
            if reverse == False :
                reverse = True
            else :
                reverse = False
        elif f == "D" :
            if not numbers :
                print("error")
                return False
            if reverse == False :
                numbers.popleft()
            else :
                numbers.pop()
    return True


t = int(input())


for i in range (t) :
    reverse = False
    func = list(input())
    n = int(input())
    if n > 0 :
        numbers = deque(map(int,input().strip("[]").split(",")))
    else :
        input()
        numbers = deque()

    if process() :
        ans = []
        while numbers :
            if reverse == False :
                ans.append(str(numbers.popleft()))
            else :
                ans.append(str(numbers.pop()))
        print("["+",".join(ans) + "]")


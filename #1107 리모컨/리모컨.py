

def changeNumber(n, brokens) :
    up = n
    down = n
    while True :
        upch = set(list(str(up)))
        downch = set(list(str(down)))
        upFlag = False
        downFlag = False
        if down >= 0 and "+" not in brokens :
            for button in downch :
                if button in brokens :
                    down -= 1
                    downFlag = True
                    break
            if not downFlag :
                return down
        if "-" not in brokens :
            for button in upch :
                if button in brokens :
                    up += 1
                    upFlag = True
                    break
            if not upFlag :
                return up


def calculatePure(n) :
    if n > 100:
        return n - 100
    elif n < 100:
        return 100 - n
    return 0

def solution() :
    n = int(input())
    m = int(input())
    if n == 100 :
        print(0)
        return
    if m == 0 :
        print(min(len(str(n)), calculatePure(n)))
        return

    brokens = list(input().split())
    count = 0
    for i in range (10) :
        if str(i) in brokens :
            count += 1

    #숫자 버튼이 다 고장난 경우 +,-로만 움직임
    if count == 10 :
        print(abs(n - 100))
        return

    changedNum = changeNumber(n, brokens)



    count = min(abs(changedNum - n) + len(str(changedNum)), calculatePure(n))
    print(count)

solution()

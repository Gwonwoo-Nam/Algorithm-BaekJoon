n = int(input())

# Square Root인지 검사

# 세 제곱의 합인지 검사
def checkSqrt(n) :
    for i in range (1,230) :
        if i*i == n :
            return True
    return False

def checkDouble(n) :
    for i in range (1,230) :
        for j in range (1,230) :
            if i*i + j*j == n :
                return True
        j = 1
    return False

def checkTriple(n) :
    for i in range (1,230) :
        for j in range (1,230) :
            for k in range (1,230) :
                if i*i + j*j + k*k == n :
                    return True
            k = 1
        j = 1
    return False

if checkSqrt(n) :
    print(1)
else :
    if checkDouble(n) :
        print(2)
    else :
        if checkTriple(n) :
            print(3)
        else :
            print(4)


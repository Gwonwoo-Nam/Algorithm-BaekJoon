from collections import defaultdict
def compare(keyA,keyB,keyC) :
    return strComp(keyA, keyB) + strComp(keyB, keyC) + strComp(keyC, keyA)

def strComp(a,b) :
    count = 0
    for i in range(len(a)) :
        if a[i] != b[i] :
            count += 1
    return count
t = int(input())

def run() :
    dic = defaultdict(int)
    n = int(input())
    cases = list(input().split())
    for case in cases :
        dic[case] += 1

    for key in dic.keys() :
        if dic[key] >= 3 :
            print(0)
            return


    m = 1000000
    for keyA in dic.keys() :
        if dic.get(keyA) :
            dic[keyA] -= 1
            for keyB in dic.keys() :
                if dic.get(keyB) :
                    dic[keyB] -= 1
                    for keyC in dic.keys() :
                        if dic.get(keyC) :
                            dic[keyC] -= 1
                            m = min(m, compare(keyA,keyB,keyC))
                            dic[keyC] += 1
                    dic[keyB] += 1
            dic[keyA] += 1
    print(m)


for i in range(t) :
    run()



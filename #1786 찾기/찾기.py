T = input()
P = input()


def createTable(P) :
    i, j = 1, 0
    table = [0 for i in range(len(P))]
    while i < len(P) :
        while j > 0 and P[i] != P[j] :
            j = table[j-1]
        if P[i] == P[j] :
            j += 1
            table[i] = j
        i += 1
    return table


li = []
count = 0
def KMP(P, T) :
    global count
    table = createTable(P)
    # j가 Pattern의 인덱스
    i, j = 0, 0
    while i < len(T) :
        while j > 0 and P[j] != T[i] :
            j = table[j-1]

        if P[j] == T[i] :
            if j == len(P) - 1 :
                li.append(i - len(P) + 2)
                count += 1
                j = table[j]
            else :
                j += 1
        i += 1

KMP(P,T)
print(count)
print(" ".join(map(str,li)))


n = int(input())

numbers = list(map(int, input().split()))
origin = numbers.copy()
numbers.sort()

di = dict()
counter = 0
for idx in range(n) :
    if numbers[idx] not in di.keys() :
        di[numbers[idx]] = counter
        counter += 1
for number in origin :
    print(di[number], end=" ")

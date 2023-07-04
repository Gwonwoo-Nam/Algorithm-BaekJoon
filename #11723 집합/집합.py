import sys
m = int(input())

s = set()
fullset = set([i for i in range(1,21)])
for _ in range (m) :
    command = sys.stdin.readline().rstrip()
    if len(command.split()) > 1 :
        val = int(command.split()[1])

    if command.startswith("add") :
        s.add(val)
    elif command.startswith("remove") :
        s.discard(val)
    elif command.startswith("check") :
        if val in s :
            print(1)
        else :
            print(0)
    elif command.startswith("toggle") :
        if val in s :
            s.discard(val)
        else :
            s.add(val)
    elif command.startswith("all") :
        s = fullset
    elif command.startswith("empty") :
        s.clear()
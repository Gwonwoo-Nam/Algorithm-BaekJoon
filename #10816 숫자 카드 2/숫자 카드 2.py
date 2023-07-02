n = input()

cards = list(map(int, input().split()))
mapping = dict()
for i in cards :
  if i not in mapping :
    mapping[i] = 1
  else :
    mapping[i] += 1

m = input()
inputs = list(map(int, input().split()))

answer = []
for i in inputs :
  if i not in mapping :
    answer.append(0)
  else :
    answer.append(mapping[i])


print(' '.join(map(str, answer)))
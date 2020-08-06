from itertools import permutations 

def concatenationsSum(a):
  a = [str(x) for x in a]
  res = list(permutations(a, 2)) 
  for i in (a):
    res.append((i, i))
  resSum = 0
  for a,b in res:
    resSum += int((a)+(b))
  return resSum

a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
a = [8]
print(concatenationsSum(a))

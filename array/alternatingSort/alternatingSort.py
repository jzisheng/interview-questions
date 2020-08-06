'''

'''

def alternatingSort2(a):
  b = []
  aa = a[:]
  while aa:
    b.append(aa.pop(0))
    if aa:
      b.append(aa.pop())
  res = all(i < j for i, j in zip(b, b[1:])) 
  return res

def alternatingSort(a):
  i, j = 0,len(a)-1
  while i < j:
    print("{} {}".format(a[i],a[j]))
    if a[i] >= a[j]: return False
    i+=1
    j-=1
  if len(a) %2 != 0:
    print (a[i])
    print(a[len(a)//2])
    return a[j-1] < (a[len(a)//2])
  return True

a = [1, 4, 5, 6, 3]
#    1 3 4 5 6

a = [0, 2, 4, 5, 3, 1]

a = [1, 3, 5, 6, 4, 2]

a = [-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48]

a = [-52, 2, 31, 56, 47, 29, -35] # True

a = [1, 3, 4, 6, 5] # False
#    1 5 3 6 4


a = [-52, 2, 31, 56, 47, 29, -35] # True


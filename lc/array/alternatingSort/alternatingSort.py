'''

'''


def isEven(a):
  n = len(a)
  i, j = 0, -1
  while i < n // 2:
    if a[i] > a[j]:
      return False
    i += 1
    j -= 1
  return True
  pass

def isOdd(a):
  i, j = 0, -1
  n = len(a)  
  while i < n // 2:
    if a[i] > a[j]:
      return False
    i += 1
    j -= 1
  return a[i] > a[i+1]

def alternatingSort(a):
  n = len(a)  
  if n == 1:
    return True
  elif n%2 == 0:
    return isEven(a)
  else:
    return isOdd(a)

a = [1, 4, 5, 6, 3]

a = [0, 2, 4, 5, 3, 1]

a = [1, 3, 5, 6, 4, 2]

a = [-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48]

a = [-52, 2, 31, 56, 47, 29, -35] # True


#    1 5 3 6 4

a = [-52, 2, 31, 56, 47, 29, -35] # True
a = [1, 3, 4, 6, 5] # False
print(alternatingSort(a))

def mutateTheArray(n, a):
  b = [0]*n
  for i  in range(n):
    n1 = 0 if i-1 < 0 else a[i-1]
    n2 = a[i]
    n3 = 0 if i+1 >= len(a) else a[i+1]
    b[i] = n1+n2+n3
  return b
n = 5
a = [4, 0, 1, -2, 3]

print(mutateTheArray(n,a))

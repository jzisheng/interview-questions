def getLesser(array, target):
    res = []
    for n in array[1:]:
        if n < target:
            res.append(n)
    return res

def getGreater(array, target):
    res = []
    for n in array[1:]:
        if n >= target:
            res.append(n)
    return res

def sameBsts(arrayOne,arrayTwo):
    print(arrayOne,arrayTwo)
    if len(arrayOne) != len(arrayTwo):
        return False
    if not(arrayOne) and not(arrayTwo):
        return True
    
    if arrayOne[0] != arrayTwo[0]:
        return False
    
    val = arrayOne[0]
    l1 = getLesser(arrayOne, val)
    l2 = getLesser(arrayTwo, val)

    g1 = getGreater(arrayOne, val)
    g2 = getGreater(arrayTwo, val)
    
    return sameBsts(l1, l2) and sameBsts(g1, g2)

###
a1 = [10, 15, 8, 12, 94, 81, 5, 2, 11]
a2 = [10, 8, 5, 15, 2, 12, 11, 94, 81]

a1 = [10, 15, 8, 12, 94, 81, 5, 2, 10]
a2 = [10, 8, 5, 15, 2, 10, 12, 94, 81]
print(sameBsts(a1,a2))

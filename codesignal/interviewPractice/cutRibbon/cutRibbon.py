
def getLen(arr, target):
    # get number of pieces that can be created
    # with length k
    res = 0
    for n in arr:
        print("{} // {}  = {}".format(n,target, n//target))
        res += n//target
    return res

def cutRibbon(arr, k):
    mx = max(arr)
    lo, hi = 1, mx
    # Start with the largest size, if not possible
    # then go to the next smallest
    while lo <= hi:
        mid = ( (hi-lo)/2 ) + lo
        print("{} {} {}".format(lo,mid, hi))
        ll = getLen(arr, mid)
        if ll >= k:
            lo = mid+1
        else:
            hi = mid-1
    return hi
        


arr = [1, 2, 3, 4, 9]
k = 5

print(cutRibbon(arr,k))

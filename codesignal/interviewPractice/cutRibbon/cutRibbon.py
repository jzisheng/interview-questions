def getPieces(arr, ll):
    # where ll is ribbon len
    res = 0
    for n in arr:
        res += n//ll
    return res

def cutRibbon(arr, k):
    lo, hi = 0, max(arr)
    while lo <= hi:
        mid = lo+((hi-lo)//2)
        npieces = getPieces(arr,mid)
        if npieces > mid:
            lo = mid+1
        else:
            hi = mid-1
    return hi


arr = [1, 2, 3, 4, 9]
k = 5

print(cutRibbon(arr,k))

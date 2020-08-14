from collections import defaultdict
def containsCloseNums(nums, k):
    m = {}
    for idx,n in enumerate(nums):
        if n in m:
            if abs(idx-m[n]) <= k: return True
        m[n] = idx
    return False

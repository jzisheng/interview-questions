'''
Imagine you're given an array that is _almost_ sorted, but not quite sorted. In
addition to this partially sorted array, you're given an integer 'k' which signifies
how far away any index i is from it's correctly sorted position. Return a sorted version
of the list, making the average time complexity as fast as possible.

Inputs
arr = [2 4 17 1 38 199 52 18]
k = 4

Outputs
[1 2 4 17 18 38 52 199]

'''

import heapq

def fun(arr,k):
    heap = []
    res = []
    i = 0
    
    while i < len(arr):
        if len(heap) <= k:
            cur  = arr[i]
            if heap and cur < heap[0]:
                res.append(cur) # 1
            else:
                heapq.heappush(heap, cur) # log n
                pass
            i += 1
        else:
            while len(heap) > k:
                if heap and i < len(arr) and arr[i] < heap[0]:
                    res.append(arr[i]) # n
                    i += 1
                else:
                    num = heapq.heappop(heap)                    
                    res.append(num)
        
    while heap:
        num = heapq.heappop(heap) 
        res.append(num) # n                
    return res

arr = [2,4,17,1,38,199,52,18]
k = 4
print(fun(arr,k))
assert(fun(arr,k) == [1,2,4,17,18,38,52,199])

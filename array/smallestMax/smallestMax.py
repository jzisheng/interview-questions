'''
Return the smallest positive integer that doesn't occur in A
'''

def solution(A):
    curMin = max(A)+1
    for i in range(max(A)+1,0,-1):
        if i not in A:
            curMin = min(curMin,i)
    if curMin > 0:
        return curMin
    return 1
print(solution([-1,-3]))

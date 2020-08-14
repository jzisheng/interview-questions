
def minSumStairsWithHops(steps, k):
    memo = {}
    
    def f(idx):
        if idx in memo:
            return memo[idx]
        elif idx >= len(steps):
            return 0
        else:
            res = []
            currCost = steps[idx]
            for ns in range(1, k+1):
                res.append(currCost+f(idx+ns))
            memo[idx] = min(res)
            return memo[idx]
    
    return f(0)


cost = [1, 5, 3, 2, 6, 1]
print(minSumStairsWithHops(cost, 2))

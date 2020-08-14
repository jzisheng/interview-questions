import math

def numSquares(n):
    squareNums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
    dp = [float('inf')]*(n+1)

    dp[0] = 0
    dp[1] = 1
    for i in range(1, n+1):
        for j in range(1, int(math.sqrt(i))+1):
            square = j*j
            dp[i] = min(dp[i], dp[i-square]+1)
    return dp[n]

# 12-4 0
# 8-4 1
# 4-4 2
# 0 1==count
print(numSquares(3))

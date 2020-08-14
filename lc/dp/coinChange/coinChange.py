import collections


class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] = min(dp[i],dp[i-coin]+1)
            pass
        result = dp[amount]
        if result != float('inf'):
            return result
        else:
            return -1
    pass

s = Solution()

coins = [1,2,5]
amount = 11
print(s.coinChange(coins,amount))
coins

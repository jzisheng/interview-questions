'''
  1      2     3
        1-2
'''

class Solution:
    def maxProfit(self, prices):
        sold = float('-inf')
        held = float('-inf')
        reset = 0
        for price in prices:
            temp = sold
            sold = held+price
            held = max(held, reset-price)
            reset = max(reset, temp)
        return max(sold,reset)
        pass
    def maxProfit2(self,prices):
        L = len(prices)
        MP = [0]*(L+2)
        for i in range(L-1,-1,-1):
            a = 0
            for sell in range(i+1, L):
                profit = (prices[sell] - prices[i])+MP[sell+2]
                a = max(profit, a)
            b = MP[i+1]
            MP[i] = max(a,b)
        return MP[0]
    pass


prices = [1,2,3,0,2]
s = Solution()
print(s.maxProfit2(prices))

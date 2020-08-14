class Solution:
    def climbStairs(self,n):
        memo = {}
        def f(step):
            if step in memo:
                return memo[step]
            if step < 0:
                return 0
            elif step == 0:
                return 1
            memo[step] =  f(step-1) + f(step-2)
            return memo[step]
            pass
        return f(n)
        pass
    pass

s = Solution()
print(s.climbStairs(2))

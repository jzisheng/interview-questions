class Solution:
    def mincostTickets(self, days, costs):
        dayset = set(days)
        if not days:
            return 0
        memo = {}
        def dp(day):
            if day > 365:
                return 0
            if day in memo:
                return memo[day]
            elif day in dayset:
                a = dp(day+1)+costs[0]
                b = dp(day+7)+costs[1]
                c = dp(day+30)+costs[2]
                memo[day] = min(a,b,c)
                return min(a,b,c)
            else:
                return dp(day+1)
        return dp(days[0])
    pass


s = Solution()
days = [1,4,6,7,8,20]
costs = [2,7,15]
print(s.mincostTickets(days,costs))
print(s.mincostTickets([],costs))


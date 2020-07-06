# 'coin change' problem
class Solution:
    def mincostTickets(self,days,costs):
        memo = {}
        if not days: return 0
        def dp(idx,day):
            if idx >= len(days):
                return 0
            elif day in memo:
                return memo[day]
            elif days[idx] > 365:
                return 0
            elif days[idx] < day:
                return dp(idx+1,day)
            else:
                a = dp(idx+1,days[idx]+1)+costs[0]
                b = dp(idx+1,days[idx]+7)+costs[1]
                c = dp(idx+1,days[idx]+30)+costs[2]
                result = min(a,b,c)
                memo[day] = result
                return result
            pass
        return dp(0,days[0])
    pass



s = Solution()
days = [1,4,6,9,10,11,12,13,14,15,16,17,18,20,21,22,23,27,28]
costs = [3,13,45]
print(s.mincostTickets(days,costs))
print(s.mincostTickets([],costs))


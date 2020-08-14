class Solution:
    def genPaths(self, r, c, m, n):
        dirs = [(0, 1), (1, 0)]
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < m and 0 <= nc < n:
                yield (nr, nc)
    
    def uniquePaths(self, m, n):
        memo = {}
        def f(r, c):
            if (r,c) in memo:
                return memo[(r, c)]
            if r == m-1 and c == n-1:
                return 1
            paths = 0
            for nr, nc in self.genPaths(r, c, m, n):
                paths += f(nr, nc)
            memo[(r, c)] = paths
            return paths
        return f(0, 0)


    def uniquePathsTabulated(self, m, n):
        dp = [[1]*n for _ in range(m)]
        for r in range(m-2,-1,-1):
            for c in range(n-2,-1,-1):
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
        return dp[0][0]

s = Solution()
print(s.uniquePathsTabulated(1, 1))

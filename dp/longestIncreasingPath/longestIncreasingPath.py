

class Solution:
    def longestIncreasingPath(self, matrix):
        if not(matrix):
            return 0
        self.m, self.n = len(matrix), len(matrix[0])
        self.dp = [[0]*self.n for _ in range(self.m)]
        self.matrix = matrix
        ans = 0
        for r in range(self.m):
            for c in range(self.n):
                ans = max(ans, self.dfs(r, c))
                print(self.dp)
        return ans


    def nextPositions(self, r, c):
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        for dr, dc in dirs:
            rr, cc = r+dr, c+dc
            if 0 <= rr < self.m and 0 <= cc < self.n:
                yield (rr, cc)

    def dfs(self, r, c):
        if self.dp[r][c] == 0:
            for rr, cc in self.nextPositions(r, c):
                if self.matrix[r][c] < self.matrix[rr][cc]:
                    self.dp[r][c] = max(self.dp[r][c], self.dfs(rr, cc))
        return 1+self.dp[r][c]

nums =  \
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
    

s = Solution()
print(s.longestIncreasingPath(nums))


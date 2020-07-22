'''
https://leetcode.com/problems/critical-connections-in-a-network/discuss/625102/Python-Clean-Concise-Tarjan-Algorithm-and-Video-Explanation
'''
from collections import defaultdict


class Solution:
    def dfs(self, node, parent, dist):
        self.low[node] = dist
        for nei in self.graph[node]:
            if nei != parent:
                if not self.low[nei]:
                    self.dfs(nei, node, dist+1)
                if self.low[nei] <= dist:
                    self.low[node] = min(self.low[node], self.low[nei])
                else:
                    self.res.append([node, nei])
        pass
    
    def criticalConnections(self, n, connections):
        self.low = [0]*n
        self.res = []
        self.graph = defaultdict(list)

        for a, b in connections:
            self.graph[a].append(b)
            self.graph[b].append(a)

        self.dfs(0, -1, 1)
        return self.res
        pass

s = Solution()
n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
s.criticalConnections(n, connections)

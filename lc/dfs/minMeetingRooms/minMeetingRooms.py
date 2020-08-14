from collections import deque, defaultdict

class Solution:
    def dfs(self, node, parent, reachable):
        self.low[node] = reachable

        for nei in self.graph[node]:
            if nei != parent:
                # if the node has not been visited
                if not self.low[nei]:
                    self.dfs(nei, node, reachable+1)
                # 
                if self.low[nei] > reachable:
                    self.res.append([node, nei])
                else:
                    self.low[node] = min(self.low[node], self.low[nei])
        pass
    
    def criticalConnections(self, n, connections):
        # Make graph
        self.graph = defaultdict(list)
        for a, b in connections:
            self.graph[a].append(b)
            self.graph[b].append(a)
        
        # Start SCC
        self.low = [0]*n
        self.res = []
        self.dfs(0,-1,1)
        return self.res
        pass


s = Solution()
connections = [[0,1],[1,2],[2,0],[1,3]]
n = 4
s.criticalConnections(n, connections)

import collections

class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        self.graph = collections.defaultdict(list)
        for a, b, weight in edges:
            self.graph[a].append((b, weight))
        for a in self.graph:
            self.graph[a].sort(key=lambda x:x[1])
        
        print(self.graph)
        
        for node in range(n):
            self.bfs(node)
        pass

    def bfs(self, node):
        stack = []
        pass


s = Solution()
n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold = 4
s.findTheCity(n, edges, distanceThreshold)

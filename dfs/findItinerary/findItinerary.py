import collections
import heapq


class Solution():
    def findItinerary(self, tickets):
        self.graph = collections.defaultdict(list)
        for a, b in tickets:
            self.graph[a].append(b)
        for a in self.graph:
            self.graph[a].sort()
        
        self.result = []
        self.dfs("JFK")
        return self.result[::-1]

    def dfs(self, node):
        destlist = self.graph[node]
        while destlist:
            nei = destlist.pop(0)
            self.dfs(nei)
        self.result.append(node)
        return
    pass


s = Solution()
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK","SFO"], ["JFK","ATL"], ["SFO","ATL"],
           ["ATL","JFK"], ["ATL","SFO"]]

res = s.findItinerary(tickets)
print(res)

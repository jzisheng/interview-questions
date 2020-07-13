import collections


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
        while self.graph[node]:
            self.dfs(self.graph[node].pop())
        self.result.append(node)
    pass


s = Solution()
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK","SFO"], ["JFK","ATL"], ["SFO","ATL"],
           ["ATL","JFK"], ["ATL","SFO"]]

res = s.findItinerary(tickets)
print(res)

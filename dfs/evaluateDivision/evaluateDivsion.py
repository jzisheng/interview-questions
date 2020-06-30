import collections
class Solution:
    def buildGraph(self,equations,values):
        for idx,(a,b) in enumerate(equations):
            self.vals[a] = values[idx]
            
        for a,b in equations:
            self.graph[a].append((b,self.vals[a]))
            self.graph[b].append((a,1/self.vals[a]))            
            pass
        
    def calcEquation(self,equations,values,queries):
        self.graph = collections.defaultdict(list)
        self.vals = {}
        # first build the graph
        self.buildGraph(equations,values)
        # then explore the query
        ans = [-1]*len(queries)

        for idx,(qa, qb) in enumerate(queries):
            self.visiting = set()
            if qa in self.graph:
                ans[idx] = float(self.dfs(qa,qb,1))
            else:
                ans[idx] = float(-1)
        return ans
        pass

    def dfs(self,start,end,product):
        if start in self.visiting:
            return -1
        self.visiting.add(start)
        if start == end:
            return product
        ans = -1
        for nei,val in self.graph[start]:
            res = self.dfs(nei,end,product*val)
            if res != -1:
                ans = res
            pass
        return ans
    pass

equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
s = Solution()
print(s.calcEquation(equations,values,queries))
 

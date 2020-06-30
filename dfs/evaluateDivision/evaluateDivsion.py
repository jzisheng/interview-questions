import collections

class Solution:
    def buildGraph(self,equations,values):
        for idx,(a,b) in enumerate(equations):
            self.vals[a] = values[idx]            
            self.graph[a].append((b,self.vals[a]))
            self.graph[b].append((a,1/self.vals[a]))            
            pass


    def dfs(self,start,end,product):
        if start in self.visited:
            return False
        if start == end and end in self.graph:
            self.result.append(product)
            return True
        self.visited.add(start)
        for nei,val in self.graph[start]:
            if self.dfs(nei,end,product*val):
                return True
        self.visited.remove(start)
        return False
    pass
        
    def calcEquation(self,equations,values,queries):
        self.graph = collections.defaultdict(list)
        self.vals = {}
        # first build the graph
        self.buildGraph(equations,values)
        # then explore the query
        self.result = []
        for idx,(qa, qb) in enumerate(queries):
            self.visited = set()            
            if  not(self.dfs(qa,qb,1)): self.result.append(-1)
        return self.result
        pass

equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
s = Solution()
print(s.calcEquation(equations,values,queries))
 

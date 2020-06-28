'''
Considering that I'ld would like to spread a promotion message across all 
people in twitter. Assuming the ideal case, if a person tweets a message,
 then every follower will re-tweet the message.

You need to find the minimum number of people to reach out (for example,
 who doesn't follow anyone etc) so that your promotion message is spread 
out across entire network in twitter.

Also, we need to consider loops like, if 
A follows B, B follows C, C follows D, D follows A (A -> B -> C -> D -> A) 
then reaching only one of them is sufficient to spread your message.

Input: A 2x2 matrix like below. In this case, a follows b, b follows c, 
c follows a.

   a b c
a  1 1 0
b  0 1 1
c  1 0 1


   0 1 2
0  1 1 0
1  0 1 1
2  1 0 1

a [a,c]
b [a,b]
c [b,c]

Output: List of people to be reached to spread out message across 
everyone in the network.

SOLUTION:
Does a topological sort and returns the first index.
TODO: return only nodes with no parents, and no cycles
'''

class Solution:
    def buildGraph(self,matrix):
        self.numParents = defaultdict(int)
        self.graph = defaultdict(list)
        for a,row in enumerate(matrix):
            for b,col in enumerate(row):
                if col:
                    self.graph[a].append(b)
            pass
        pass
    
    def dfs(self,node):
        if node in self.visiting or node in self.visited:
            return
        self.visiting.add(node)
        for nei in self.graph[node]:
            if nei not in self.visited:
                self.dfs(nei)
                if nei != node:
                    self.numParents[nei] += 1
            pass
        self.visiting.remove(node)                
        self.visited.add(node)
        self.res.append(node)
        pass
    
    def minimumMessage(self,matrix):
        self.visited,self.visiting = set(), set()
        self.paths = []
        self.res = []
        self.buildGraph(matrix)
        # now perform topological sort
        for node in self.graph:
            self.res = []
            self.dfs(node)
            if self.res:
                self.paths.append(self.res)
        result = []
        for path  in self.paths:
            result.append(path[-1])
        return result

    pass

print("")
matrix = [[1,1,0],[0,1,1],[1,0,1]]
s = Solution()
print(s.minimumMessage(matrix))
    

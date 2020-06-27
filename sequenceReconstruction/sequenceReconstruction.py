'''
Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.
'''
import collections
class Solution:
    def sequenceReconstruction(self, org, seqs):
        self.buildGraph(seqs)
        
        # explore forwards, backwards dfs
        a = self.dfsExplore(org)
        b = self.dfsExplore(org[::-1])
        print(a)
        print(b)
        return a == b

    def dfsExplore(self,order):
        self.visiting = set()
        self.visited = set()
        self.topo = []        
        for node in order:
            self.dfs(node)
        return (self.topo[::-1])
    
    def dfs(self,node):
        if node in self.visiting or node in self.visited:
            # detects if cycle, or already visited
            return
        self.visiting.add(node)
        for nei in self.graph[node]:
            self.dfs(nei)
            pass
        self.visiting.remove(node)
        self.visited.add(node)
        self.topo.append(node)
        pass
        
    def buildGraph(self,seqs):
        self.graph = collections.defaultdict(list)        
        for seq in seqs:
            if len(seq) == 1:
                self.graph[seq[0]]
            for i in range(1,len(seq)):
                a,b = seq[i-1],seq[i]
                self.graph[a].append(b)
                pass
            pass
        pass
    pass



print("")
s = Solution()


org = [4,1,5,2,6,3]
seqs = [[5,2,6,3],[4,1,5,2]]
print(s.sequenceReconstruction(org,seqs))


# this should return false
# two ways to construct:
# [1,2,3]
# [1,3,2]
'''
org, seqs = [1],[]
print(s.sequenceReconstruction(org,seqs))

org = [1,2,3]
seqs = [[1,2],[1,3]]
print(s.sequenceReconstruction(org,seqs))



org = [1,2,3]
seqs = [[1,2]]
print(s.sequenceReconstruction(org,seqs))


'''

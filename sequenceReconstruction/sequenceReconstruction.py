'''
Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.
'''
import collections
class Solution:

    def makeGraph(self,org,seqs):
        self.graph = collections.defaultdict(list)
        self.numParents = collections.defaultdict(int)
        self.nodes = set()
        for seq in seqs:
            self.nodes = self.nodes.union(set(seq))
            for i in range(1,len(seq)):
                a,b = seq[i-1],seq[i]
                self.graph[a].append(b)
                self.numParents[b] += 1
        pass
    
    def sequenceReconstruction(self, org, seqs):
        self.makeGraph(org,seqs)
        exploreNodes,res = [],[]        
        # explore nodes with no parents
        for node in org:
            if self.numParents[node] == 0:
                exploreNodes.append(node)
            pass
        for node in exploreNodes:
            self.dfs(node)
        
    def dfs(self,node):
        pass
    pass



print("")
s = Solution()

# False
org = [1,2,3]
seqs = [[1,3],[1,2]]

print(s.sequenceReconstruction(org,seqs))

'''
org = [4,1,5,2,6,3]
seqs = [[5,2,6,3],[4,1,5,2]]


org, seqs = [1], [[],[]]


# False
org = [1,2,3]
seqs = [[2,3]]

'''
# false




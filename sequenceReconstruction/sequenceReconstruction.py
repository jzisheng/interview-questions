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
        exploreNodes = []
        stack = []
        # explore nodes with no parents
        for node in self.nodes:
            if self.numParents[node] == 0:
                stack.append(node)
            pass
        res = []
        while stack:
            if len(stack) != 1:
                return False
            node = stack.pop(0)
            res.append(node)
            for nei in self.graph[node]:
                self.numParents[nei] -= 1
                if self.numParents[nei] == 0:
                    stack.append(nei)
            pass
        return len(res) == len(self.nodes) and res == org
            
print("")
s = Solution()
org,seqs = [1,2,3], [[1,2],[1,3],[2,3]] # true
print(s.sequenceReconstruction(org,seqs))

'''
org,seqs = [1,2,3],[[1,2],[1,3],[2,3]] # True
org,seqs = [4,1,5,2,6,3], [[5,2,6,3],[4,1,5,2]] # True
org, seqs = [1], [[],[]] # False
org,seqs = [1,2], [[1,2],[2,1]] # false
org,seqs = [1,2], [[1,2],[2,1]] # false
org,seqs = [1,2,3], [[1,2],[1,3],[2,3]] # true
org,seqs = [1,2,3], [[1,2],[1,3],[2,3]] # true
org, seqs = [1,2,3], [[2,3]] # False

'''
# false




import collections
class Solution:
    def buildGraph(self,seqs):
        self.graph = collections.defaultdict(list)        
        for seq in seqs:
            if len(seq) == 1:
                self.graph[seq[0]]
            for i in range(1,len(seq)):
                a,b = seq[i-1],seq[i]
                self.graph[a].append(b)
                self.graph[b].append(a)

    def sequenceReconstruction(self, org, seqs):
        self.buildGraph(seqs)

        
# this should return false
# two ways to construct:
# [1,2,3]
# [1,3,2]
s = Solution()
print(s.sequenceReconstruction([1,2,3],[[1,2],[1,3]]))
org = [4,1,5,2,6,3]
seqs = [[5,2,6,3],[4,1,5,2]]
print(s.sequenceReconstruction(org,seqs))

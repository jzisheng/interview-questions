'''
0
hit
012

''+'it'

'''
import collections

class Solution:
    def bfs(self, curWord, endWord, path):
        queue = []
        queue.append((curWord, 0))
        visited = set()
        while queue:
            cur, path = queue.pop(0)
            if cur == endWord:
                return path+1
            if cur in visited:
                continue
            visited.add(cur)
            for idx in range(len(cur)):
                neighbors = self.graph[cur[:idx]+"*"+cur[idx+1:]]
                for nei in neighbors:
                    queue.append((nei, path+1))
        return 0

    
    def ladderLength(self, beginWord, endWord, wordList):
        self.graph = collections.defaultdict(list)
        for word in wordList:
            for idx in range(len(word)):
                self.graph[word[:idx]+"*"+word[idx+1:]].append(word)
        return self.bfs(beginWord, endWord, 0)
        pass

    
s = Solution()
beginWord = "hit"
endWord = "log"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

#beginWord = "aa"
#endWord = "da"
#wordList = ["ba","da"]

s.ladderLength(beginWord, endWord, wordList)

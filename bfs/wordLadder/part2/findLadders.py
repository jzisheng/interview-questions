'''
012
hit
:i, idx+1:
*it
h*t
hi*


hit -> h*t

'''

import collections
class Solution():
    def bfs(self, beginWord, endWord, res):
        queue = []
        visited = set()
        
        queue.append((beginWord, [beginWord]))
        maxLen = float('inf')
        
        while queue:
            cur, cpath = queue.pop(0)
            if cur == endWord:
                maxLen = min(maxLen, len(cpath))
                if True or len(cpath) <= maxLen:
                    res.append(cpath)
                continue
            if cur in visited:
                print(cur)
                continue
            visited.add(cur)
            for nw in self.generateWords(cur):
                for nei in self.graph[nw]:
                    queue.append((nei, cpath+[nei]))
        pass

    def generateWords(self, word):
        for idx in range(len(word)):
            yield word[:idx]+'*'+word[idx+1:]

    def findLadders(self, beginWord, endWord, wordList):
        self.graph = collections.defaultdict(list)
        if endWord not in wordList:
            return []
        for word in wordList:
            for nw in self.generateWords(word):
                self.graph[nw].append(word)
                pass
        print(self.graph['*ex'])
        res = []
        self.bfs(beginWord, endWord, res)
        return res


s = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

beginWord = "a"
endWord = "c"
wordList = ["a","b","c"]

beginWord = "red"
endWord = "tax"
wordList = ["ted","tex","red","tax","tad","den","rex","pee"]

print(s.findLadders(beginWord, endWord, wordList))

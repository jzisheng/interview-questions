class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self,word):
        node = self.root()
        for w in word:
            if w in node.children:
                node = node.children.get(w)
            else:
                return False
        return node.isWord
    
        
class Solution():
    def nextPositions(self, r, c):
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        for dr,dc in dirs:
            nR, nC = r+dr, c+dc
            if 0 <= nR < self.m and 0 <= nC < self.n:
                yield (nR, nC)
        pass

    def findWords(self, board, words):
        self.m, self.n = len(board), len(board[0])

        res = []
        trie = Trie()
        node = trie.root
        
        for w in words:
            trie.insert(w)

        for r in range(self.m):
            for c in range(self.n):
                self.dfs(board, node, r, c, "", res)
        
        return res
    
    def dfs(self, board, node, r, c, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        tmp = board[r][c]
        node = node.children.get(tmp)
        if not node:
            return
        board[r][c] = '#'
        for nR, nC in self.nextPositions(r,c):
            self.dfs(board, node, nR, nC, path+tmp, res)
            board[r][c] = tmp

s = Solution()
'''


'''
board = [["a","a"]]
words = ["aaa"]

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]




s.findWords(board, words)

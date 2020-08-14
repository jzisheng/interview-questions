import collections
def exist(board,word):    
    def dfs(board,r,c,idx,word):
        if (r,c) in visited: return False
        if r < 0 or r >= len(board):
            return False
        if c < 0 or c >= len(board[0]):
            return False
        if idx >= len(word):
            return True
        if board[r][c] != word[idx]:
            return False
        visited.add((r,c))
        if dfs(board,r+1,c,idx+1,word) or \
           dfs(board,r-1,c,idx+1,word) or \
           dfs(board,r,c+1,idx+1,word) or \
           dfs(board,r,c-1,idx+1,word):
            return True
        return False

    letterMaps = collections.defaultdict(list)
    for r,row in enumerate(board):
        for c,char in enumerate(row):
           letterMaps[char].append((r,c))
        pass
    for (r,c) in letterMaps[word[0]]:
        visited = set()
        if dfs(board,r,c,0,word): return True
    return False
    


board =\
[\
  ['A','B','C','E'],\
  ['S','F','C','S'],\
  ['A','D','E','E']\
]

word = "DEE"

print(exist(board,word))

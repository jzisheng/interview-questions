from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.isWord = True
        
    def search(self, word):
        """
        Returns if the word is in the data structure. 
        A word could contain the dot character '.' to 
        represent any one letter.
        """
        def f(node, idx):
            if idx == len(word):
                return node.isWord
            c = word[idx]
            if c in node.children:
                # c is in node children
                return f(node.children[c],idx+1)
            elif c == '.':
                # c is a wildcard
                for child in node.children.keys():
                    if f(node.children[child], idx+1): return True
                return False
            else:
                # not in children and not a '.'
                return False
        return f(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
param_2 = obj.search("bad")
param_2 = obj.search("ba.")
param_2 = obj.search(".ad")
print(param_2)


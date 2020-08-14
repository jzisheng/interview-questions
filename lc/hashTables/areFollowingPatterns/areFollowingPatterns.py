from collections import defaultdict
def areFollowingPatterns(strings,patterns):
    dPtr = {}
    dStr = {}
    for i in range(len(strings)):
        p, s = patterns[i], strings[i]
        if s in dStr and dStr[s] != p: return False
        if p in dPtr and dPtr[p] != s: return False
        dPtr[p] = s
        dStr[s] = p
    return True


strings = ["cat", "dog",  "dog"]
patterns = ["a", "b", "c"]

strings = ["cat", "dog", "doggy"]
patterns = ["a", "b", "b"]


strings = ["cat", "dog",  "dog"]
patterns = ["a",  "b",  "b"]

print(areFollowingPatterns(strings,patterns))

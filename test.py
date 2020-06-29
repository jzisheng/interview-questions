def letterCombinations(digits):
    # Write your code here
    letterMap = ["","","abc","def","ghi","jkl","mno","pqrs",
                "tuv","wxyz"]
    idx = 0
    curstr = []
    

    def dfs(idx,s=""):
        if len(s) >= len(digits):
            curstr.append(s)
            return
        key = int(digits[idx])
        letters = letterMap[key]
        for c in letters:
            dfs(idx+1,s+c)
        pass
    dfs(0)
    return curstr

def restoreIpAddresses(s):
    # must be between 0 and 255
    result = []
    def dfs(idx, resStr=[]):
        if idx >= len(s):
            print(".".join(resStr))
            return
        temp = int(s[idx:idx+3])
        if 0 <= temp <= 255:
            dfs(idx+3,resStr+[str(temp)])
            pass
        pass
    dfs(0)
    return result
    pass


print(restoreIpAddresses("25525511135"))
        

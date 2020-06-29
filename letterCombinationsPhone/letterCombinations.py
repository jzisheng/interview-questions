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

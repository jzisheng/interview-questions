
'''
93. Restore IP Address DFS
'''
def isValid(s):
    if s and 0 <= int(s) <= 255 and s[0] != 0:
        return True
    return False
    
def restoreIpAddresses(s):
    # must be between 0 and 255
    result = []
    def dfs(idx, resStr=[]):
        if idx >= len(s) and len(resStr) <= 4:
            resStr = ".".join(resStr)
            if resStr not in result: result.append(resStr)
            return
        strIp = s[idx:idx+2]
        if isValid(strIp) and len(resStr) <= 4:
            dfs(idx+2,resStr+[str(strIp)])
            pass
        pass        
        strIp = s[idx:idx+3]
        if isValid(strIp) and len(resStr) <= 4:
            dfs(idx+3,resStr+[str(strIp)])
            pass
        pass
    dfs(0)
    return list(result)
    pass


print(restoreIpAddresses("25525511135"))

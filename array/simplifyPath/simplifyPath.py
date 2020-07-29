'''
"/a/./b/../../c/"
a  .  b  ..  ..  c
            ^
 
if . ignore
if .. pop off stack
else append to stack
'''

class Solution:
    def simplifyPath(self, path):
        if not path: return ""
        dirs = path.split("/")
        res = []
        for d in dirs:
            if d:
                if d == '.':
                    continue
                if d == '..':
                    if res: res.pop()
                else:
                    res.append(d)
        return "/"+"/".join(res)
        pass


s = Solution()
path = "/a/./b/../../c/"
path = "/home//foo/"
path = "/a//b////c/d//././/.."
print(s.simplifyPath(path))

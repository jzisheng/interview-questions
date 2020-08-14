class Solution:
    def minRemoveToMakeValid(self, s):
        toRemove = []
        stack = []
        s = list(s)
        for idx, c in enumerate(s):
            if len(stack) == 0 and c == ')':
                toRemove.append(idx)
            elif c == ')' and stack:
                stack.pop()
            elif c == '(':
                stack.append(idx)
        toRemove.extend(stack)
        for remove in toRemove:
            s[remove] = ''
        return "".join(s)


s = Solution()
print(s.minRemoveToMakeValid("))(("))

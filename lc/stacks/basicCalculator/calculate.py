'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), 
the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

'''

class Solution:
    def evalStack(self, stack):
        res = 0 if not stack else int(stack.pop())
        # input stack, returns int
        while stack and stack[-1] != ")":
            sign = stack.pop()
            if sign == '-':
                res -= int(stack.pop())
            elif sign == '+':
                res += int(stack.pop())
        return res
        
    def calculate(self, s):
        s.replace(" ","")
        cur = ""
        stack = []
        operands = {"+","-",")"}
        
        for i in range(len(s)-1,-1,-1):
            if s[i].isdigit():
                cur = s[i]+cur
            else:
                print(cur,stack)
                # not a digit
                if cur: stack.append(cur)
                # is operator
                if s[i] in operands: stack.append(s[i])
                # eval stack
                elif s[i] == "(":
                    res = self.evalStack(stack)
                    stack.pop()
                    stack.append(res)

                # reset cur string
                cur = ""                    
        if cur:
            stack.append(cur)
        res = self.evalStack(stack)
        return res
        pass


s = "16-(2+3)"

sol = Solution()
print(sol.calculate(s))
# assert sol.calculate(s) == 4

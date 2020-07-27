class Solution:
    def multiply(self, num1, num2):
        res = [0]*(len(num1)+len(num2))
        pos = len(res)-1
        for n1 in num1[::-1]:
            temp = pos
            for n2 in num2[::-1]:
                res[temp] += int(n1)*int(n2)
                res[temp-1] += res[temp]//10
                res[temp] %= 10
                temp -= 1
                pass
            pos -= 1
            pass
        while len(res)>1 and res[0] == 0:
            res.pop(0)
        return "".join([str(x) for x in res])
        

s = Solution()
num1, num2 = '0', '0'
s.multiply(num1, num2)

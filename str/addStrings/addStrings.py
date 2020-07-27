class Solution:
    def addStrings(self, num1, num2):
        res = []
        carry = 0
        i, j = len(num1)-1, len(num2)-1
        while i >= 0 or j >= 0:
            a = ord(num1[i])-ord('0') if i >= 0 else 0
            b = ord(num2[j])-ord('0') if j >= 0 else 0
            val = (a+b+carry) % 10
            carry = (a+b+carry) // 10
            res.append(val)
            i -= 1
            j -= 1
        
        if carry:
            res.append(carry)
        return ''.join(str(x) for x in res[::-1])
        pass


s = Solution()
num1, num2 = "99", "9"
print(s.addStrings(num1, num2))


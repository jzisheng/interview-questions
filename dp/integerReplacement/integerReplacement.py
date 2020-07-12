class Solution():
    def integerReplacement(self, n):
        def f(n):
            if n < 1:
                return float('inf')
            elif n == 1:
                return 0
            elif n % 2 == 0:
                a = 1+f(n/2)
                return a
            else:
                b, c = f(n-1)+1, f(n+1)+1
                return min(b, c)
        return f(n)
        pass


s = Solution()
print(s.integerReplacement(5))

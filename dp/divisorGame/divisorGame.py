class Solution:
    def divisorGame(self, N):
        alice = 0
        while True:
            for x in range(1,N):
                if N%x == 0:
                    alice += 1
                    N -= x
                    break
            if N%2 != 0:
                break
        if alice % 2 == 0:
            return False
        else:
            return True
    pass
s = Solution()
print(s.divisorGame(10))

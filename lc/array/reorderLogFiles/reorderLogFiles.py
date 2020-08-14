'''
letter logs come before any digit log

letter logs are ordered lexicographically by the log text, then by identifier(for tie break)

digit logs put in original order

'''


class Solution:
    def reorderLogFiles(self, logs):
        def f(log):
            lid, lstr = log.split(" ", 1)
            if lstr[0].isalpha():
                return (0, lstr, lid)
            return (1,)
        logs.sort(key=f)
        return logs
        pass


s = Solution()
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]
print(s.reorderLogFiles(logs))

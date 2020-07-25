from collections import defaultdict


class Solution:
    def leastInterval(self, tasks, n):
        d = defaultdict(int)
        for i in tasks:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        lst = sorted(d.values(), reverse=True)
        max_number = lst[0]

        i = 0
        counter = 0
        while i < len(lst) and lst[i] == max_number:
            counter += 1
            i += 1

        ret = (max_number-1) * (n+1) + counter
        return max(ret, len(tasks))
        pass


s = Solution()

tasks = ["A","A","A","B","B","B"]
n = 2
s.leastInterval(tasks, n)

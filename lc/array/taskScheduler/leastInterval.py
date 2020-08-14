from collections import defaultdict

class Solution:
    def leastInterval(self, tasks, n):
        counts = defaultdict(int)
        for t in tasks:
            counts[t] += 1
        # after getting counts of all elements
        lst = sorted(counts.values())
        maxNumber = lst[-1]
        counter = 0
        while lst and lst[-1] == maxNumber:
            lst.pop()
            counter += 1
        ret = (maxNumber-1)*(n+1)+counter
        print("{} {}".format(len(tasks),ret))        
        return max( len(tasks), ret )

s = Solution()

tasks = ["A","A","A","B","B","B"]
n = 2
print(s.leastInterval(tasks, n))

from heapq import heappush, heappop, heappushpop

class MedianFinder:
    def __init__(self):
        self.smaller = [] # max heap
        self.larger = [] # min heap
        
    def addNum(self, num):
        val = heappushpop(self.smaller,-num)
        heappush(self.larger,-val)
        if len(self.smaller) < len(self.larger):
            val = heappop(self.larger)
            heappush(self.smaller,-val)
        pass
    
    def findMedian(self):
        if len(self.smaller) == len(self.larger):
            a,b = -self.smaller[0],self.larger[0]
            return (a+b)/2
        else: 
            return -self.smaller[0]


mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
assert(mf.findMedian() == 1.5)
mf.addNum(3)
assert (mf.findMedian() == 2.0)


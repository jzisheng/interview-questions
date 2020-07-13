import collections
import heapq

class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        graph = collections.defaultdict(list)

        for a, b, w in edges:
            graph[a].append((b, w))
            graph[b].append((a, w))

        def numNeighbors(city):
            queue = [(city, 0)]
            visited = set()

            while queue:
                weight, node = heapq.heappop(queue)
                if node in visited:
                    continue
                if node != city:
                    visited.add(node)
                for nei, nwei in graph[node]:
                    if nei in visited:
                        continue
                    if weight+nwei <= distanceThreshold:
                        heapq.heappush(queue, (weight+nwei, nei))
            return len(visited)

        res = []
        for city in range(n):
            res.append((numNeighbors(city), city))
        res.sort(key=lambda x: (-x[0], x[1]))
        return res[-1][1]
        pass

    
s = Solution()
n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold = 4

'''
n = 5
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distanceThreshold = 2
'''

print(s.findTheCity(n, edges, distanceThreshold))

'''
People hazards
You are tasked to create every possible subset of various people. 
Some people hate other people.
All people are arranged in a row, numbered consecutivley from
1 to n in order. Given a list of which people dislike others, 
determine number of intervals of people that contain subsets
 that can coexist

n = 3
a = [2,1,3]
p = [3,3,1]
3 is poisonous to 2
3 is poisonous to 1
1 is poisonous to 3
'''
from collections import defaultdict
def peopleHazard(n,a,p):
    graph = defaultdict(list)
    for idx in range(len(a)):
        personA,personB = a[idx],p[idx]
        graph[personA].append(personB)
    result = []
    # [1,2,3]
    people = list(range(1,n+1))
    def dfs(prev,idx,cur=[]):
        if idx >= n:
            if (cur) and cur not in result:
                result.append(cur)
            return
        a = people[idx]
        if a not in graph[prev]:
            dfs(a,idx+1,cur+[a])
        dfs(a,idx+1,cur)
    for i in range(n):
        node = people[i]
        dfs(None,i)
    return result
    pass

print("")
n = 3
a = [2,1,3]
p = [3,3,1]
print(peopleHazard(n,a,p))

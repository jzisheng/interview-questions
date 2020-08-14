
from collections import defaultdict


def find_roots(graph, candidates):
    children = set()
    for a in graph.keys():
        for c in graph[a]:
            children.add(c)
    return candidates.difference(children)
    pass

def dfs(node, depth, graph):
    if node == None: return
    print("{} {}".format('  '*depth, node))
    for child in graph[node]:
        dfs(child, depth+1, graph)


def organize(input):
    # base case no input check
    if not(input): return
    graph = defaultdict(set)
    roots = set()
    
    for a,b in input:
        roots.add(a)
        roots.add(b)
        graph[a].add(b)

    roots = find_roots(graph,roots)
    
    for r in roots:
        dfs(r, 0, graph)

input = [['Macos','Apple'],['Sports','bat'],['bat','cricket'],
         ['Windows', 'dell'],['Computers', 'Macos'],['Computers', 'Windows']]
organize(input)

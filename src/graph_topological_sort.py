from collections import defaultdict
from pprint import pprint
class Solution(object):
    def __init__(self, v):
        self.V = v
        self.g = defaultdict(list)
        
    def addedge(self, k, v):
        self.g[k].append(v)
        
    def topological_sort(self, vertex, visited, stack):
        visited[vertex] = True
        for node in self.g[vertex]:
            print "node ",node
            if not visited[node]:
                self.topological_sort(node, visited, stack)

        stack.insert(0,vertex)
        print 'stack ',stack

if __name__ == "__main__":
    g = Solution(4)
    #g.addedge(3,1)
    g.addedge(3,2)
    g.addedge(1,2)
    g.addedge(0,2)
    g.addedge(0,1)

    print g.g
    visited = [False] * g.V
    stack = []
    inVertices = defaultdict(int)
    
    for i in range(g.V):
        for j in g.g[i]:
            inVertices[j] += 1
    print inVertices

    for i in range(g.V):
        if not visited[i]:
            g.topological_sort(i, visited, stack)

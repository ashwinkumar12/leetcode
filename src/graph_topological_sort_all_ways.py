from collections import defaultdict
from pprint import pprint
class Solution(object):
    def __init__(self, v):
        self.V = v
        self.g = defaultdict(list)
        
    def addedge(self, k, v):
        self.g[k].append(v)
        
    def topological_sort(self, visited, stack, inVertices):

        for i in range(self.V):
            if not visited[i] and inVertices[i] == 0:
                visited[i] = True
                stack.append(i)
                for node in self.g[i]:
                    inVertices[node] -= 1
                self.topological_sort(visited, stack, inVertices)
            visited[i] = False
            stack.pop(-1)
            for node in self.g[i]:
                inVertices[node] += 1
            flag = True

        print 'stack ',stack

if __name__ == "__main__":
    g = Solution(4)
    g.addedge(3,1)
    g.addedge(3,2)
    g.addedge(1,2)
    g.addedge(0,2)
    g.addedge(0,1)
    visited = [False] * g.V
    stack = []
    inVertices = defaultdict(int)

    for k,v in g.g.iteritems():
        print k,v
    for i in range(g.V):
        for j in g.g[i]:
            inVertices[j] += 1
    print inVertices

    for i in range(g.V):
        if not visited[i]:
            g.topological_sort(visited, stack, inVertices)
            stack = []
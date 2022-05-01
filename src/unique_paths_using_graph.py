from collections import defaultdict
from pprint import pprint
class Solution(object):
    def __init__(self):
        self.no_ways = 0
        self.g = defaultdict(list)
        self.paths = 0
        
    def addedge(self, k, v):
        self.g[k].append(v)
        
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        c = m
        r = n
        self.form_graph(c,r)
        if not self.g:
            return 1
        pprint(dict(self.g))
        last_node = str(r-1)+str(c-1)
        self.dfs('00',last_node)
        return self.paths
    
    def form_graph(self, c, r):        
        for j in range(r):
            for i in range(c):
                if j+1<=r-1:
                    self.addedge(str(j)+str(i),str(j+1)+str(i))
                if i+1<=c-1:
                    self.addedge(str(j)+str(i),str(j)+str(i+1))
                    
    def dfs(self, start_node, last_node):
        for node in self.g[start_node]:
            #print node
            if node == last_node:
                self.paths += 1
                return
            self.dfs(node, last_node)

print Solution().uniquePaths(2,3)

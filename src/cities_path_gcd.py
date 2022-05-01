from collections import defaultdict

class Solution():
	def __init__(self):
		self.graph=defaultdict(list)
		self.paths=[]
	
	def add_edge(self,u,v):
		self.graph[u].append(v)

	def find_path(self, vertex,dest, visited, path):
		visited[vertex-1] = True
		path.append(vertex)
		if vertex==dest:
			print path
			self.paths.append(path)
		for value in self.graph[vertex]:
			print visited
			print 'value --- ',value
			if not visited[value-1]:
				self.find_path(value,dest,visited,path)
		path.pop()
		visited[vertex-1] = False
		#print path
		return path

s=Solution()

s.add_edge(1,2)
s.add_edge(1,3)
s.add_edge(2,5)
s.add_edge(2,4)
s.add_edge(2,6)
s.add_edge(3,6)

print s.graph
visited = [None]*7
print s.find_path(1,6,visited,[])

print s.paths

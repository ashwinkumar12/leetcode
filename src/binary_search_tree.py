from collections import defaultdict
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		
		#for vertical sum
		self.value = None
		self.sum_dict = defaultdict(int)

	def insert(self, data):
		if self.data:
			if data < self.data:
				if not self.left:
					self.left = Node(data)
				else:
					self.left.insert(data)
			else:
				if not self.right:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data

	def print_tree(self):
		#print '\n' ,self.data
		if self.left:
			self.left.print_tree()
		print self.data
		if self.right:
			self.right.print_tree()

	def print_data(self):
		return self.data

	def dfs(self):
		#print 'data - '+str(self.data)
		if self.left:
			self.left.print_tree1()
		print self.data
		if self.right:
			self.right.print_tree1()

	def bfs(self, curr_level, data):
		#print 'printing starting curr_level'
		#self.next_level_data(curr_level)
		next_level = list()
		for level in curr_level:
			if level.data == data:
				return level.data
			if level.left:
				if level.left.data == data:
					print 'Matched - ',level.left.data
					return level.left.data
				next_level.append(level.left)
				print "printing left next_level_data"
				self.next_level_data(next_level)
			if level.right:
				if level.right.data == data:
					print 'Matched - ',level.right.data
					return level.right.data
				next_level.append(level.right)
				print "printing right next_level_data"
				self.next_level_data(next_level)
			#print next_level

		if next_level:
			answer = self.bfs(next_level,data)
		else:
			print 'No match found'
			return
		return answer

	def next_level_data(self, next_level):
		print "len - ",len(next_level)
		for level in next_level:
			print 'data - ', level.data

	def diagonal_sum(self, current_level):
		curr_sum = 0
		next_level = list()
		print "current_level - ",self.next_level_data(current_level)
		for curr_level in current_level:
			while curr_level:
				print "curr_level - ",curr_level.data
				curr_sum += curr_level.data
				if curr_level.left:
					next_level.append(curr_level.left)
				curr_level = curr_level.right

		print "curr_sum - ",curr_sum
		print "next_level - ",self.next_level_data(next_level)
		if next_level:
			self.diagonal_sum(next_level)

	def vertical_sum(self, curr_level):
		next_level = list()
		for node in curr_level:
			self.sum_dict[node.value] += node.data
			if node.left:
				node.left.value = node.value - 1
				next_level.append(node.left)
			if node.right:
				node.right.value = node.value + 1
				next_level.append(node.right)
		if next_level:
			self.vertical_sum(next_level)
		return self.sum_dict

if __name__ == "__main__":
	root = Node(10)
	root.value = 0
	root.insert(13)
	root.insert(11)
	root.insert(8)
	root.insert(9)
	root.insert(4)
	root.insert(41)
	# root.insert(5)
	# root.insert(6)
	# root.insert(2)
	# root.insert(3)

	root.print_tree()

	#print 'data ' + str(root.print_data())

	#print root.bfs([root], 101)
	print "\n"
	#root.diagonal_sum([root])
	print root.vertical_sum([root])
	"""
				10
		8				13
	
	4		9		11 		 41
	"""

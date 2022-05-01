class Heap(object):
	def __init__(self):
		self.heap_array = [0]
		self.curr_size = 0

	def insert(self, value):
		self.heap_array.append(value)
		self.curr_size+=1
		self.perc_up(self.curr_size)

	def delete_min(self):
		self.heap_array[1], self.heap_array[-1] = self.heap_array[-1],self.heap_array[1]
		self.perc_down(1)
		self.curr_size-=1
		return self.heap_array.pop()

	def perc_up(self, i):
		while i//2 > 0:
			#print self.heap_array[i//2], self.heap_array[i//2 +1], self.heap_array[i]
			if self.heap_array[i//2] > self.heap_array[i]:
				self.heap_array[i//2],self.heap_array[i] = self.heap_array[i], self.heap_array[i//2]
			i = i//2

	def perc_down(self,i):
	    while (i * 2) <= self.curr_size:
	        mc = self.minChild(i)
	        if self.heap_array[i] > self.heap_array[mc]:
	            self.heap_array[i],self.heap_array[mc] = self.heap_array[mc],self.heap_array[i]
	        i = mc

	def minChild(self,i):
	    if i * 2 + 1 > self.curr_size:
	        return i * 2
	    else:
	        if self.heap_array[i*2] < self.heap_array[i*2+1]:
	            return i * 2
	        else:
	            return i * 2 + 1	

	def build_heap(self, heap_list):
		self.heap_array = [0] + heap_list
		self.curr_size = len(heap_list)
		i = self.curr_size // 2
		print self.heap_array
		while i>0:
			self.perc_down(i)
			print self.heap_array
			i -= 1

a = Heap()
a.build_heap([112, 12, 121, 23, 2311, 122, 42, 232, 1000])
print a.heap_array
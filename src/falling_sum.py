from collections import defaultdict
class Solution(object):
	def __init__(self):
		self.min_value = defaultdict(dict)
	def find_min_sum(self, arr):
		size = len(arr[0])
		for i in range(len(arr)-1,-1,-1):
			for j in range(size):
				self.min_value[i][j] = arr[i][j]
		print self.min_value
		for i in range(len(arr)-2,-1,-1):
			for j in range(size):
				allowed_range = range(max(j-1,0), min(min(j+1,size)+1,size) )
				self.min_value[i][j] = arr[i][j] + min([self.min_value[i+1][a] for a in allowed_range])
		return min([self.min_value[0][i] for i in range(size)])

	def minFallingPathSum(self, A):
		"""
		:type A: List[List[int]]
		:rtype: int
		"""
		return self.find_min_sum(A)

if __name__ == "__main__":
	a = Solution()
	print a.minFallingPathSum([	[1,2,3],
								[4,5,6],
								[7,8,9]	]
							 )
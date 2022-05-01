from collections import defaultdict
a = [2,7,9,3,1]

def house_robber(arr):
	sum = defaultdict(int)
	for i in range(len(arr)-1,-1,-1):
		sum[i] = arr[i] + max(sum[i+2],sum[i+3])
	print sum

house_robber(a)
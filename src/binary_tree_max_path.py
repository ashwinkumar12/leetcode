def max_path(node,res):
	max1 = node.value
	if node.left:
		max2 = max_path(node.left)
	if node.rigt:
		max3 = max_path(node.right)
	max4 = max1+max2+max3

	maxi = max(max1,max1+max2,max1+max3,max4)
	res = max(maxi,res)
	return res

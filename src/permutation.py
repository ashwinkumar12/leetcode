def permutation(lst): 
	print "lst ",lst
	if len(lst) == 0: 
		return [] 
	if len(lst) == 1: 
		return [lst] 
	l = []
	for i in range(len(lst)):
		m = lst[i] 
		print "m ",m
		remLst = lst[:i] + lst[i+1:] 
		a = permutation(remLst)
		print a
		for p in a:
			l.append([m] + p)
		print l 
	return l 

# Driver program to test above function 
data = list('123') 
print permutation(data)

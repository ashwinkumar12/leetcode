sum = 0

def max_transported_amount(mat, r, c):
	global sum
	print "entry ",r,c,sum
	if c==-1 or r==-1:
		return sum

	print r+1,c+1
	print "row ",mat[r][:c+1]
	print "column ",[mat[4+r-k][c] for k in range(r+1)]

	row_sum = reduce(lambda a,b:a+b ,mat[r][:c+1])
	col_sum = reduce(lambda a,b:a+b, [mat[4+r-k][c] for k in range(r+1)])
	print row_sum, col_sum

	if row_sum > col_sum:
		r -= 1
		sum += row_sum
		print "row picked ",sum
	else:
		c -= 1
		sum += col_sum
		print "column picked ",sum
	max_transported_amount(mat, r, c)

if __name__=="__main__":
	mat = [
[0 ,0 ,10 ,9], #West
[1 ,3 ,10 ,0],
[4 ,2 ,1 ,3],
[1 ,1 ,20 ,0],
[10 ,0 ,0 ,0] ,#North
[1 ,1 ,1 ,30],
[0 ,0 ,5 ,5],
[5 ,10 ,10 ,10]
]
	r = len(mat)/2
	c = len(mat[0])
	print r-1, c-1, "\n "
	max_transported_amount(mat,r-1,c-1)
	print sum
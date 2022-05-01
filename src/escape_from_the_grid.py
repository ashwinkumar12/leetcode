#four_ways
row = [-1,0,0,1]
column = [0,1,-1,0]

#eight_ways
row = [-1,-1,-1,0,0,1,1,1]
column = [0,-1,1,1,-1,0,-1,1]

import sys
min_dist = sys.maxint

def start_position(mat,r,c):
	for i in range(r):
		for j in range(c):
			if mat[i][j] == 2:
				return i,j

def is_safe(mat, r, c, i, j):
	if i>=0 and i<r and j>=0 and j<c and mat[i][j]==0:
		return True
	else:
		return False

def is_boundary(r,c,i,j):
	if i==0 or j==0 or i==r-1 or j==c-1:
		return True
	else:
		return False

def find_shortest_dist(mat, r, c, i, j, dist):
	global min_dist
	if is_boundary(r,c,i,j):
		min_dist = min(min_dist,dist)
		print "inside is_boundary - ", min_dist
		return min_dist

	for direction in range(len(row)):
		print row[direction], column[direction]
		if is_safe(mat,r,c,i+row[direction],j+column[direction]):
			next_i,next_j = i+row[direction],j+column[direction]
			print i,j,next_i,next_j
			print mat
			dist += 1
			mat[next_i][next_j] = 1
			print mat
			find_shortest_dist(mat,r,c,next_i,next_j,dist)
			mat[next_i][next_j] = 0
			dist -= 1
			print mat," backtrack"
			
	return min_dist

if __name__=="__main__":
	mat = [
[1,0,0,0],
[0,0,2,1],
[0,0,0,0],
[0,1,1,0]
]
	r = len(mat)
	c = len(mat[0])
	i,j = start_position(mat,r,c)
	dist = 0
	print mat, r, c, i, j, dist, min_dist, "\n "
	print find_shortest_dist(mat,r,c,i,j,dist)

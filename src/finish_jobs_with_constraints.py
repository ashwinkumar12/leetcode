""" Given an array of jobs with different time requirements. There are K identical assignees available and we are also
given how much time an assignee takes to do one unit of the job. Find the minimum time to finish all jobs with following
constraints.

An assignee can be assigned only contiguous jobs. For example, an assignee cannot be assigned jobs 1 and 3, but not 2.
Two assignees cannot share (or co-assigned) a job, i.e., a job cannot be partially assigned to one assignee and
partially to other. Input :

K:     Number of assignees available. 
T:     Time taken by an assignee to finish one unit  of job 
job[]: An array that represents time requirements of  different jobs. 

Examples :

Input:  k = 2, T = 5, job[] = {4, 5, 10} 
Output: 50 The minimum time required to finish all the jobs is 50. There are 2
assignees available. We get this time by  assigning {4, 5} to first assignee and {10} to second  assignee.

Input:  k = 4, T = 5, job[] = {10, 7, 8, 12, 6, 8} 
Output: 75 We get this time by assigning {10} {7, 8} {12} and {6, 8}
"""
import sys

def isPossible(k,job,mid):
	n = 0
	temp = 0
	for i,j in enumerate(job):
		print temp
		temp+=j
		if temp>=mid:
			temp = j
			n+=1
	if temp>mid:
		n+=1
	print n,k
	return k>=n

def calculate(k,t,job):
	high = sum(job)
	low = 0
	min_time = sys.maxint
	while low<high:
		mid = low + (high-low)/2
		print job
		print low,mid,high,min_time
		if isPossible(k,job,mid):
			high = mid
			min_time = min(mid, min_time)
		else:
			low = mid + 1
		print low,mid,high,min_time
		print "\n"
	print min_time * t

if __name__ == "__main__":
	k = 4
	t =5
	job = [10,7,8,12,6,8]
	calculate(k,t,job)
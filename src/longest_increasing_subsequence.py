from collections import Counter
class Solution(object):
    def longestIncreasingSubSeq(self, s, n):
    	if n-1>0 and s[n] < s[n-1]:
    		return 0
    	elif n-1>0 and s[n] > s[n-1]:
    		return self.longestIncreasingSubSeq(s, n-1)+1
    	else:
    		return max(self.longestIncreasingSubSeq(s, n-1),self.longestIncreasingSubSeq(s, n-2))

a = [1,2,6,4,7]
print a
print Solution().longestIncreasingSubSeq(a,len(a)-1)
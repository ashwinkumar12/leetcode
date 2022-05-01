from collections import Counter
class Solution(object):
    def longestPalindromeSubseq(self, s, m, n):
        if m==n:
            return 1
        if s[m]==s[n]:
            return 2 + self.longestPalindromeSubseq(s,m+1,n-1)
        else:
            return max(self.longestPalindromeSubseq(s,m+1,n), self.longestPalindromeSubseq(s,m,n-1))
        return l

a = 'BBABCBCAB'
print a
print Solution().longestPalindromeSubseq(a,0,len(a)-1)
class Solution(object):
    def longestCommonSubseq(self,a,b,m,n):
        if m==0 or n==0:
            return 0
        elif a[m-1]==b[n-1]:
            return 1 + self.longestCommonSubseq(a,b,m-1,n-1)
        else:
            return max(self.longestCommonSubseq(a,b,m-1,n), self.longestCommonSubseq(a,b,m,n-1))
        return l

a = 'BBABCBCAB'
b = 'BBAsdA'
print a,b
print Solution().longestCommonSubseq(a,b,len(a),len(b))
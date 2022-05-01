class Solution(object):
    def __init__(self):
        self.dp = {1:1,2:1}

    def integerBreak(self, n):
        if n in self.dp:
            return self.dp[n]
        a = n/2
        b = n - a
        result = list()
        while 1:
            #print result,a,b
            if a<1 or b>n:
                break
            self.dp[a] = self.integerBreak(a)
            self.dp[b] = self.integerBreak(b)
            result.append(max((self.dp[a]*self.dp[b]),(a*b),(a*self.dp[b]),(b*self.dp[a])))
            a -= 1
            b += 1
        self.dp[n] = max(result)
        #print self.dp
        return max(result)

a = Solution()
print "Enter the number"
n = raw_input()
print a.integerBreak(int(n))
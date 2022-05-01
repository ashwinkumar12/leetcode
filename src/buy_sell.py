import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        max_profit = 0
        max_profit1 = 0
        a = 0
        b = len(prices)-1
        
        while a<b:
            #print prices[a],prices[b]
            if prices[b] > prices[a]:
                diff = prices[b]-prices[a]
                b -= 1
            else:
                diff = 0
                a += 1
            if diff > max_profit:
                max_profit = diff
            #print max_profit

        a1 = 0
        b1 = len(prices)-1
        while a1<b1:
            #print prices[a],prices[b]
            if prices[b1] > prices[a1]:
                diff = prices[b1]-prices[a1]
                a1 += 1
            else:
                diff = 0
                b1 -= 1
            if diff > max_profit1:
                max_profit1 = diff
            #print max_profit
            
        return max(max_profit,max_profit1)
        """

        """
        Brute force
            max_profit = 0
            for i in range(len(prices)):
                for j in range(i+1,len(prices)):
                    diff = 0
                    #print i,j,prices[i],prices[j]
                    if prices[i]<prices[j]:
                        diff = prices[j] - prices[i]
                    if diff>max_profit:
                        max_profit = diff
                    #print max_profit
            return max_profit
        """
        max_profit = 0
        min_value = sys.maxint
        for i in range(len(prices)-1):
            if prices[i] < min_value:
                min_value = prices[i]
            elif prices[i] - min_value > max_profit:
                max_profit = prices[i] - min_value
        return max_profit

prices = [3,2,6,5,0,3]
print Solution().maxProfit(prices)
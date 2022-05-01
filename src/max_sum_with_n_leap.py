class Solution(object):
    def __init__(self):
        self.max_cost_dict = dict()
    def max_sum_n_leap(self, cost, n):
        result = self.cost_max(cost,n)    
        return result
    def cost_max(self,cost,n):
        if len(cost)-1 in self.max_cost_dict:
            return self.max_cost_dict[len(cost)-1]
        if not cost:
            return 0
        self.max_cost_dict[len(cost)-1] = cost[-1] + max([self.cost_max(cost[:-i],n) for i in range(1,n+1)])
        return self.max_cost_dict[len(cost)-1]

cost = [1,10,-1,-2]

a = Solution()
print a.max_sum_n_leap(cost,1)
print a.max_cost_dict
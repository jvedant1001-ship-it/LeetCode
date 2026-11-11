class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        price1 = cost1*need1 + cost2*need2
        price2 = max(need1,need2)*costBoth
        price3 = min(need1, need2) * costBoth + abs(need1 - need2) * (cost1 if need1 > need2 else cost2)
        final = min (price1 ,price2 ,price3)
        return final
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """

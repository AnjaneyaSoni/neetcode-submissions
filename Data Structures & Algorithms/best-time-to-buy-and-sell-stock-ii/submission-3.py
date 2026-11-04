class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res=0
        for x in range (len(prices)-1):
            if prices[x+1]>prices[x]:
                res+=(prices[x+1]-prices[x])
        return res
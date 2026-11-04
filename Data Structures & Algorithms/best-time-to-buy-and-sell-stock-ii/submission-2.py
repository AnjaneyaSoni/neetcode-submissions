class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        i=0
        res=0
        l=len(prices)
        while i<(l-1):
            if min<prices[i+1]:
             
                while (i+1)<l:
                    
                    if prices[i]>prices[i+1]:
                        res+=prices[i]-min
                        min=prices[i+1]
                        i+=1
                    else:                       
                        i+=1
                        if (i+1)==l:
                            res+=prices[i]-min
                            return res
            else:
                min=prices[i+1]
                i+=1
        return res
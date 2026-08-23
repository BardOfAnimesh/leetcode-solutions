class Solution(object):
    def maxProfit(self, prices):
        maximum=0
        l = 0
        r=1
        while(r<len(prices)):
            if prices[r]<prices[l]:
                l+=1
            elif prices[r]==prices[l]:
                r+=1
            elif prices[r]>prices[l]:
                maximum=max(maximum,prices[r]-prices[l])
                r+=1
        return maximum
        

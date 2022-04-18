class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMax = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right]-prices[left]
                currMax = max(currMax, profit)
            else:
                left = right
            
            right +=1
        
        return currMax
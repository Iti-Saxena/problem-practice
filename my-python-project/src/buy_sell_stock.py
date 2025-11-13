class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for p in prices:
            if p < min_price:
                min_price = p          # best (cheapest) buy so far
            else:
                max_profit = max(max_profit, p - min_price)  # sell today

        return max_profit
    
obj=Solution()
# print(obj.maxProfit([7,1,5,3,6,4]))  #Expected output is 5
# print(obj.maxProfit([1,2]))  #Expected output is 1
print(obj.maxProfit([2,4,1]))  #Expected output is 2
# print(obj.maxProfit([2,1,2,1,0,1,2]))  #Expected output is 2
# print(obj.maxProfit([2,4,1]))  #Expected output is 2

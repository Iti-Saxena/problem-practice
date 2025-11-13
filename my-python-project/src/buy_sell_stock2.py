class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        max_price = 0
        for p in prices:
            if p < min_price:
                min_price = p          # best (cheapest) buy so far
                 
            else:
                max_price=p
                max_profit = max_profit + (p - min_price)
                min_price=p  # sell today

        return max_profit
    
obj=Solution()
print(obj.maxProfit([7,1,5,3,6,4]))  #Expected output is 7
# print(obj.maxProfit([1,2,3,4,5])) #Expected output is 4
# print(obj.maxProfit([2,1,2,0,1])) #Expected output is 2
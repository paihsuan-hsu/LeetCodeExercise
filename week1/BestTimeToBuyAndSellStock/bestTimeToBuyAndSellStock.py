class Solution:
    @classmethod
    def bestTimeToBuyAndSellStock(self,prices: list[int])-> int:
        low = prices[0]
        max_profit=0
        for i in prices[1:]:
            print("i :"+str(i)+ "  "  +str(low) + " "+ str(max_profit)+ "\n")
            max_profit = max(max_profit, i - low)
            low = min(low, i)
        return max_profit

prices = [7,1,5,3,6,4]
output = Solution.bestTimeToBuyAndSellStock(prices)
print(output)

prices = [7,6,4,3,1]
output = Solution.bestTimeToBuyAndSellStock(prices)
print(output)
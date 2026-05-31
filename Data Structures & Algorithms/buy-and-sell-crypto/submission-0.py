class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize a left and right pointer at index 0 and 1 and max profit to be 0.
        # l = buy, r = sell.
        l, r = 0, 1
        max_profit = 0

        # Run a while loop till the right pointer is within bounds.
        while r < len(prices):
            # If the buying price is less than the selling price, calcualte the profit.
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                # Update max profit.
                max_profit = max(max_profit, profit)
            # If buying price is not less than selling price, set the buying price to the current selling price. 
            else:
                l = r
            # In all cases, move the selling price index by 1.
            r += 1
        # Return the max profit.
        return max_profit

# Time: O(n)
# Space: O(1)
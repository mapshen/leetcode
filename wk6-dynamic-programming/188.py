class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        num_of_days = len(prices)
        num_of_trades = k

        if num_of_trades * 2 < num_of_days:
            profits = [0 for _ in range(num_of_days)]

            for j in range(1, num_of_trades + 1):
                local_profit = profits[0] - prices[0]

                for i in range(1, num_of_days):
                    previous = profits[i]
                    profits[i] = max(profits[i - 1], local_profit + prices[i])
                    local_profit = max(local_profit, previous - prices[i])

            return profits[num_of_days - 1]
        else:
            profit = 0

            for i in range(1, num_of_days):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]

            return profit

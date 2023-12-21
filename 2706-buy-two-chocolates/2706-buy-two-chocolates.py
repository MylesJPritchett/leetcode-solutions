class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # Sort the prices in ascending order
        sorted_prices = sorted(prices)

        remaining_money = money - (sorted_prices[0] + sorted_prices[1])
        if remaining_money < 0:
            return money
        return remaining_money
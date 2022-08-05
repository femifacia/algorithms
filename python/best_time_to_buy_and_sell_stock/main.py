#!/usr/bin/env python3

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        size = len(prices)
        if (size == 1):
            return (0)
        buy = 0
        sell = 1
        max_profit = 0
        while (sell < size):
            profit = prices[sell] - prices[buy]
            if (prices[sell] > prices[buy]):
                max_profit = profit if profit > max_profit else max_profit
            else:
                buy = sell
            sell += 1
        return (max_profit)
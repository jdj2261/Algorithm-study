"""
Date : 21년 3월 25일
Description : Algorithm Study
Title : 주식을 사고팔기 가장 좋은 시점
"""
"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

import sys
class Solution:
    def maxProfit(self, prices: list(int)) -> int:
        profit = 0
        min_price = sys.maxsize

        # 최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price-min_price)
        return profit


        
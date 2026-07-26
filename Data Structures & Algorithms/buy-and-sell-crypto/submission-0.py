class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 0
        max_ = 0

        while right < len(prices):
            if left == right:
                right += 1
            elif prices[left] > prices[right]:
                left = right
            else:
                max_ = max(max_, prices[right] - prices[left])
                right += 1
        return max_


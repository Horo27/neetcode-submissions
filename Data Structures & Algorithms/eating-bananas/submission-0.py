class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        piles.sort()
        left, right = 1, piles[-1]
        min_rate = piles[-1]
        while left <= right:
            mid = (left + right) // 2
            time = 0
            for pile in piles:
                time += pile//mid 
                if pile % mid:
                    time+=1
            
            if time <= h:
                min_rate = min(min_rate, mid)
                right = mid - 1
            else:
                left = mid + 1
        return min_rate




        
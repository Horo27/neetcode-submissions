class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        merged = False

        for interval in intervals:
            if merged:
                res.append(interval)
                continue
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                res.append(interval)
                merged = True
            elif newInterval[0] > interval[1]:
                res.append(interval)
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        if not merged:
            res.append(newInterval)
        return res
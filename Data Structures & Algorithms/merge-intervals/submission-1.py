class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])

        res = []
        curr = None

        for interval in intervals:
            if not curr:
                curr = interval
            elif curr[1] < interval[0]:
                res.append(curr)
                curr = interval
            else:
                curr = [min(curr[0], interval[0]), max(curr[1], interval[1])]
        res.append(curr)
        return res
                
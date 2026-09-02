class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])

        i = 0 
        res = []
        curr = None

        while i < len(intervals):
            if not curr:
                curr = intervals[i]
            elif curr[1] < intervals[i][0]:
                res.append(curr)
                curr = intervals[i]
            else:
                curr = [min(curr[0], intervals[i][0]), max(curr[1], intervals[i][1])]
            i += 1
        res.append(curr)
        return res
                
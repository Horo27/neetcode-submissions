class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1]) 

        end = intervals[0][1]
        nr = 0

        for i in range(1, len(intervals)):
            if end > intervals[i][0]:
                nr += 1
                end = min(intervals[i][1], end)
            else:
                end = intervals[i][1]
        return nr


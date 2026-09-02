"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        events = []
        for interval in intervals:
            events.append(["start", interval.start])
            events.append(["end", interval.end])
        events.sort(key = lambda x : (x[1], x[0]))

        max_ = 0
        curr = 0

        for event in events:
            if event[0] == "start":
                curr += 1
                max_ = max(max_, curr)
            else:
                curr -= 1
        return max_
        
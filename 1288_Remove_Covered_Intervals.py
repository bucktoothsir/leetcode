class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = len(intervals)
        if len(intervals) <= 1:
            return res
        intervals = sorted(intervals, key=lambda interval:(interval[0], -interval[1]))
        i = 0
        j = 1
        while j < len(intervals):
            if intervals[j][1] <= intervals[i][1]:
                res -= 1
            else:
                i = j
            j += 1
        return res

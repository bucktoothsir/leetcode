class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        
        i = 0 
        j = 1
        res = 0
        
        while j < len(intervals):
            if intervals[i][1] > intervals[j][0]:
                res += 1
                if intervals[i][1] > intervals[j][1]:
                    i = j
            else:
                i = j
            j += 1
        return res

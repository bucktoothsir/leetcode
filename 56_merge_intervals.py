class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = []
        i = 0
        j = 1
        while j < len(intervals):
            if intervals[j][0] <= intervals[i][1]:
                if intervals[j][1] > intervals[i][1]:
                    intervals[i][1] = intervals[j][1]
                j += 1
            else:
                res.append(intervals[i])
                i = j
                j = i + 1
        res.append(intervals[i]) 
        return res
        

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points = sorted(points, key=lambda x:x[1])
        res = 1
        i = 0
        j = 1
        while j < len(points):
            if points[j][0] > points[i][1]:
                res += 1
                i = j
            j += 1
        return res
        
        
        

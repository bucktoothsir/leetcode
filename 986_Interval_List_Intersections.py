class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0
        j = 0
        while i < len(firstList) and j < len(secondList):
            first_interval = firstList[i]
            second_interval = secondList[j]
            start = max(first_interval[0], second_interval[0]) 
            end = min(first_interval[1], second_interval[1]) 
            if start <= end:
                res.append([start, end])
            if first_interval[1] < second_interval[1]:
                i += 1
            else:
                j += 1
        return res
   

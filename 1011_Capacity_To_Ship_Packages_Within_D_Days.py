class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        start = max(weights)
        end = max(weights) * len(weights) // D
        
        while start < end:
            mid = (start + end) // 2
            num_of_day = 0
            sum_of_w = 0
            for w in weights:
                if sum_of_w + w > mid:
                    num_of_day += 1
                    sum_of_w = w
                else:
                    sum_of_w += w
            num_of_day += 1 if sum_of_w else 0
            if num_of_day > D:
                start = mid + 1
            else:
                end = mid
        return start
                    
                    
                


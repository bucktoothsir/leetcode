class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        
        start = min(bloomDay)
        end = max(bloomDay)
        
        while start < end:
            mid = (start + end) // 2
            num_of_bouquet = 0
            i = 0
            while i < len(bloomDay):
                while i < len(bloomDay) and bloomDay[i] > mid:
                    i += 1
                j = i
                while j < len(bloomDay) and bloomDay[j] <= mid:
                    j += 1
                if i != j:
                    num_of_bouquet += (j - i) // k
                    i = j
            if num_of_bouquet < m:
                start = mid + 1
            else:
                end = mid
        return start
                    

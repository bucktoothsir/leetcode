class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_pile = min(piles)
        max_pile = max(piles)
        
        start = 1
        end = max_pile
        
        while start < end:
            mid = (start + end) // 2
            num_of_h = 0
            i = 0
            while i < len(piles):
                pile = piles[i]
                r, q = divmod(pile, mid)
                num_of_h += r
                num_of_h += 1 if q else 0
                if num_of_h > h:
                    start = mid + 1
                    break
                i += 1
            if i == len(piles):
                end = mid
        return start
                    

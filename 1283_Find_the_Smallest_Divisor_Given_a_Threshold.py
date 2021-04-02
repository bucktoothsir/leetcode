class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start = 1
        end = max(nums)
        import math
        
        while start < end:
            mid = (start + end) // 2
            num_of_res = 0
            for num in nums:
                num_of_res += math.ceil(num / mid)
            if num_of_res > threshold:
                start = mid + 1
            else:
                end = mid
        return start
                
                
        

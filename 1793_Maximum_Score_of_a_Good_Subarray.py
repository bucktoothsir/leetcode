class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        i = k
        j = k
        max_score = nums[k]
        min_num = nums[k]
        
        while i > 0 and j < len(nums) - 1:
            if nums[i-1] < nums[j+1]:
                j += 1
                min_num = min(min_num, nums[j])
            else:
                i -= 1
                min_num = min(min_num, nums[i])
            
            score = (j - i + 1) * min_num
            max_score = max(score, max_score)
        
        while i > 0:
            i -= 1
            min_num = min(min_num, nums[i])
            score = (j - i + 1) * min_num
            max_score = max(score, max_score)
            
        while j < len(nums) - 1:
            j += 1
            min_num = min(min_num, nums[j])
            score = (j - i + 1) * min_num
            max_score = max(score, max_score)
        return max_score
            
                

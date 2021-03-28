class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        partition_idx_1 = []
        partition_idx_2 = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                partition_idx_1.append(i)
                partition_idx_2.append(j)
                i += 1
                j += 1
               
        i = len(partition_idx_1) - 1
        max_sum = 0
        while i >= 0:
            if i == len(partition_idx_1) - 1:
                end1 = len(nums1)
                end2 = len(nums2)
                start1 = partition_idx_1[i] + 1
                start2 = partition_idx_2[i] + 1
            else:
                start1 = partition_idx_1[i] + 1
                start2 = partition_idx_2[i] + 1
                end1 = partition_idx_1[i+1]
                end2 = partition_idx_2[i+1]
            
            partion_num = nums1[start1-1]
            max_sum += partion_num +  max(sum(nums1[start1:end1]), sum(nums2[start2:end2]))
            i -= 1 
        if i == -1:
            end1 = len(nums1) if not partition_idx_1 else partition_idx_1[0]
            end2 = len(nums2) if not partition_idx_2 else partition_idx_2[0]
            max_sum += max(sum(nums1[0:end1]), sum(nums2[0:end2]))
        return max_sum % (10 ** 9 + 7)


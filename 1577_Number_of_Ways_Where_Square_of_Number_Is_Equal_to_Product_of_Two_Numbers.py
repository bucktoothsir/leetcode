class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        res = 0
        for num in nums1:
            square = num ** 2
            i = 0
            j = len(nums2) - 1
            while i < j:
                product = nums2[i] * nums2[j]
                if product > square:
                    j -= 1
                elif product < square:
                    i += 1
                else:
                    if nums2[i] == nums2[j]:
                         res += (j - i + 1) * (j - i) // 2
                         break
                    else:
                        start = i
                        end = j
                        while i < j and nums2[i] == nums2[i+1]:
                            i += 1
                        while i < j and nums2[j] == nums2[j-1]:
                            j -= 1
                        res += (i - start + 1) * (end - j + 1)
                        j -= 1
                            
                            
        for num in nums2:
            square = num ** 2
            i = 0
            j = len(nums1) - 1
            while i < j:
                product = nums1[i] * nums1[j]
                if product > square:
                    j -= 1
                elif product < square:
                    i += 1
                else:
                    if nums1[i] == nums1[j]:
                         res += (j - i + 1) * (j - i) // 2
                         break
                    else:
                        start = i
                        end = j
                        while i < j and nums1[i] == nums1[i+1]:
                            i += 1
                        while i < j and nums1[j] == nums1[j-1]:
                            j -= 1
                        res += (i - start + 1) * (end - j + 1)
                        j -= 1
        return res

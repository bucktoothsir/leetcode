def merge(nums1, m, nums2, n):
    if n:
        i = m - 1
        j = n - 1
        p = len(nums1) - 1
        while p >= 0 and i >= 0 and j >= 0:
            if nums2[j] > nums1[i]:
                nums1[p] = nums2[j]
                j -= 1
            else:
                nums1[p] = nums1[i]
                i -= 1
            p -= 1
        while p >= 0 and j >= 0:
            nums1[p] = nums2[j]
            p -= 1
            j -= 1

if __name__ == '__main__':
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    print(nums1)

class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        A = sweetness
        left, right = min(A), sum(A) // (K + 1)
        while left < right:
            mid = (left + right + 1) // 2
            cur = cuts = 0
            for a in A:
                cur += a
                if cur >= mid:
                    cuts += 1
                    cur = 0
            if cuts > K:
                left = mid
            else:
                right = mid - 1
        return left

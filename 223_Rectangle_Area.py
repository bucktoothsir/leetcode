class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        left = max(A, E)
        right = min(C, G)
        top = min(D, H)
        down = max(B, F)
        
        area = (D - B) * (C - A) + (G - E) * (H - F)
        if right > left and top > down:
            return area - (right - left) * (top - down)
        else:
            return area
         

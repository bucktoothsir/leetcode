class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1 = sorted(slots1)
        slots2 = sorted(slots2)
        i = 0
        j = 0
        while i < len(slots1) and j < len(slots2):
            slot1 = slots1[i]
            slot2 = slots2[j]
            if (slot1[0] < slot2[1] and slot1[1] > slot2[0]) or (slot2[0] < slot1[1] and slot2[1] > slot1[0]):
                start = max(slot1[0], slot2[0])
                end = min(slot1[1], slot2[1])
                if end - start >= duration:
                    return [start, start+duration]
            if slot1[1] > slot2[1]:
                j += 1
            else:
                i += 1
        return []

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def helper(head):
            p = ListNode()
            p = head
            q = ListNode()
            if p.next:
                q = p.next
                p.next = q.next
                q.next = p
                return q
            else:
                return p
        if head:
            head = helper(head)
            if head.next and head.next.next:
                head.next.next = self.swapPairs(head.next.next)
        return head

if __name__ == '__main__':
    nums = [2,5,3,4,6,2,2]
    head = ListNode(nums[0])
    p = head
    for n in nums[1:]:
        q = ListNode(n)
        p.next = q
        p = p.next
    s = Solution()
    head = s.swapPairs(head)
    p = head
    while p:
        print(p.val)
        p = p.next

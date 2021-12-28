def mergeTwoLists(self, list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    p1 = list1
    p2 = list2
    if not p1:
        return p2
    if not p2:
        return p1
    if p1.val <= p2.val:
        p1.next = self.mergeTwoLists(p1.next, p2)
        return p1
    else:
        p2.next = self.mergeTwoLists(p1, p2.next)
        return p2
        
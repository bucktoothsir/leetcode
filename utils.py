#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright ©  2021-12-27 17:03 bucktoothsir <rsliu.xd@gmail.com>
#
# Distributed under terms of the MIT license.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList(object):
    def __init__(self, nums):
        if nums:
            self.head = ListNode(nums[0])
            p = self.head
            for n in nums[1:]:
                p.next = ListNode(n)
                p = p.next
        else:
            self.head = None
    
    def print():
        p = self.head
        while p:
            print(p.val, end="")
            print(' ', end="")
            p = p.next


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
https://leetcode.com/problems/add-two-numbers/
Dificulty: Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each
of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

2 -> 4 -> 3
5 -> 6 -> 4
-----------
7 -> 0 -> 8

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.


Time Complexity O(max(n, m))
Space Complexity O(max(n, m))
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l3 = ListNode()
        head = l3
        carry_out = 0
        while (
            l1.next != None or l2.next != None
        ):  # at least one list must still have elements
            # if one list is shorter than the other, keep adding nodes with key 0
            if l1.next == None:
                l1.next = ListNode()
            if l2.next == None:
                l2.next = ListNode()

            s = l1.val + l2.val + carry_out
            if s >= 10:
                digit = s % 10
                l3.val = digit
                carry_out = 1
            else:
                l3.val = s
                carry_out = 0

            # iterate on all lists
            l1 = l1.next
            l2 = l2.next

            l3.next = ListNode()
            l3 = l3.next

        # last digit
        s = l1.val + l2.val + carry_out
        if s >= 10:
            digit = s % 10
            l3.val = digit
            carry_out = 1
        else:
            l3.val = s
            carry_out = 0

        if carry_out == 1:
            l3.next = ListNode(val=1)

        return head

"""
Date : 21년 3월 28일
Description : Algorithm Study
Title : 역순 연결 리스트
"""
"""
https://leetcode.com/problems/reverse-linked-list/
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            print(prev.val)
            return reverse(next, node)

        return reverse(head)
    
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            node, prev = next, node
        return prev
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next = ListNode(3)
l1.next = ListNode(2)
l1.next = ListNode(2)
Solution().reverseList()


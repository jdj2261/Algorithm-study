"""
Date : 21년 3월 28일
Description : Algorithm Study
Title : 두수의 덧셈
"""
"""
https://leetcode.com/problems/add-two-numbers/
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 연결 리스트 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            node, prev = next, node
        return prev
    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> ListNode:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    # 파이썬 리스트를 연결 리스트로 변환
    def toReverseLinkedList(self, result: ListNode) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

        return self.toReverseLinkedList(str(resultStr))
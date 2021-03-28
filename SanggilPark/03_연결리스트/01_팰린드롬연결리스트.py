"""
Date : 21년 3월 28일
Description : Algorithm Study
Title : 팰린드롬 연결 리스트
"""
"""
https://leetcode.com/problems/palindrome-linked-list/

Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 리스트 변환
    def isPalindrome(self, head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

    # 데크를 이용한 최적화
    def isPalindrome2(self, head: ListNode) -> bool:
        q: deque = deque()
        if not head:
            return True
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
        
        while q:
            if q.popleft() != q.pop():
                return False
        return True

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next = ListNode(2)
l1.next = ListNode(1)

sol = Solution()
print(sol.isPalindrome2(l1))
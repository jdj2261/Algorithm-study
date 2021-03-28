"""
Date : 21년 3월 28일
Description : Algorithm Study
Title : 페어의 노드 스왑
"""
"""
https://leetcode.com/problems/swap-nodes-in-pairs/
Input: head = [1,2,3,4]
Output: [2,1,4,3]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 값만 교환
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            cur.val, cur.next = cur.next.val, cur.val
            cur = cur.next.next
        return head
    
    # 반복 구조로 스왑
    def swapPairs2(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            # b가 a(head)를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head

            # prev가 b를 가리키도록 할당
            prev.next = b

            # 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next
        return root.next
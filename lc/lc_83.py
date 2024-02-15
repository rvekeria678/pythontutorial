# Leetcode Problem #83: Remove Duplicates

# Description: Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            while current.next and current.val == current.next.val:
                current.next = current.next.next 
            current = current.next
        return head
    def printList(self, head: Optional[ListNode]):
        current = head
        while current != None:
            print(current.val)
            current = current.next

s = Solution()

node7 = ListNode(5, None)
node6 = ListNode(4, node7)
node5 = ListNode(4, node6)
node4 = ListNode(3, node5)
node3 = ListNode(2, node4)
node2 = ListNode(1, node3)
node1 = ListNode(1, node2)

s.printList(s.deleteDuplicates(node1))
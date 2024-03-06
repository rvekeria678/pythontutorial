# Leetcode Problem #876: Middle of the Linked List

# Description: Given the head of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast, count = head, head, 0
        
        while fast != None:
            fast = fast.next
            count+=1
        
        for i in range(0,count//2):
            slow = slow.next

        return slow

s = Solution()

n4 = ListNode(5, None)
n3 = ListNode(4, n4)
n2 = ListNode(3, n3)
n1 = ListNode(2, n2)
head = ListNode(1, n1)
print(s.middleNode(head))

n5 = ListNode(6, None)
n4 = ListNode(5, n5)
n3 = ListNode(4, n4)
n2 = ListNode(3, n3)
n1 = ListNode(2, n2)
head = ListNode(1, n1)
print(s.middleNode(head))
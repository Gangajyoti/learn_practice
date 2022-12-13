"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.



Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.val)
            temp = temp.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        prev = None
        curr = head
        while curr != None:
            if curr.next == None:
                break
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head

linked_list = LinkedList()
linked_list.head = first = ListNode(1,None)
second = ListNode(1,None)
three = ListNode(2,None)

linked_list.head.next = second
linked_list.head.next.next = three

c= Solution()
outp = LinkedList()
outp.head =c.deleteDuplicates(linked_list.head)
outp.printList()

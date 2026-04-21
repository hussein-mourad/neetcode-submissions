# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        n = len(arr)
        print(arr)
        if not arr:
            return None
        new_head = ListNode(arr.pop())
        curr = new_head
        while arr:
            curr.next = ListNode(arr.pop())
            curr = curr.next
        return new_head

        
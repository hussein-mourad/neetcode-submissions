# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = list1
        while curr:
            arr.append(curr.val)
            curr = curr.next
        curr = list2
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr.sort()
        n = len(arr)
        list3 = ListNode(arr[0])
        curr = list3
        for i in range(1, n):
            curr.next = ListNode(arr[i])
            curr = curr.next
        return list3


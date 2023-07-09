# Question: https://leetcode.com/problems/merge-two-sorted-lists/

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node as the head of the merged list
        dummy = ListNode(0)
        current = dummy
        
        # Compare nodes from both lists and merge them
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append any remaining nodes from list1 or list2
        if list1 is not None:
            current.next = list1
        else:
            current.next = list2
        
        return dummy.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s // 10
            current.next = ListNode(s % 10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            current.next = ListNode(carry)
        return dummy.next

# Creating the linked lists
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

# Creating an object of the Solution class
s = Solution()

# calling the method using the class object
result = s.addTwoNumbers(l1, l2)

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next 
        prev = slow.next = None
        while second: # reversing second list portion 
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        second = prev

        # merge two halfs
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

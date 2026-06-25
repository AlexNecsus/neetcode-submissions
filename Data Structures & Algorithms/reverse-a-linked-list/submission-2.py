#  prev, cur = None, head
#  while cur:
#      tmp = cur.next
#      cur.next = prev
#      prev = cur
#      cur = tmp
#  return prev


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we save first one then we start recursing towards last node than change first last and stuff
        # then we return one after last node
        if not head: return head
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead
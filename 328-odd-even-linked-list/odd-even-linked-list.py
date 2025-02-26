class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head

        odd = head
        even = head.next
        evenStart = even


        while even != None and odd != None and even.next != None and odd.next != None:

            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
            
        odd.next = evenStart

        return head
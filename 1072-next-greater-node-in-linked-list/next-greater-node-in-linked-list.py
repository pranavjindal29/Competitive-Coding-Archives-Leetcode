# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Tuple[Optional[ListNode], int]:
        pre = None      
        l = 0  
        while head:
            l += 1            
            cur = head 
            head = cur.next
            cur.next = pre 
            pre = cur 
        
        return pre, l
    
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        new_head, l = self.reverseList(head)
        res = [0] * l
        stack  = []
        while new_head:
            l -= 1
            while stack and stack[-1] <= new_head.val:
                stack.pop()

            if stack:
                res[l] = stack[-1]
            
            stack.append(new_head.val)
            new_head = new_head.next

        return res
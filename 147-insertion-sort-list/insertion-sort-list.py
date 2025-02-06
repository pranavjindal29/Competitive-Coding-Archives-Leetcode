class Solution(object):
    def insertionSortList(self, head):

        result = ListNode(-5000)

        def insert(partial, toplace):
            initial = partial
            partial = partial.next
            while partial != None:
                if toplace < partial.val:
                    break
                initial = partial
                partial = partial.next
            newnode = ListNode(toplace)
            initial.next = newnode
            newnode.next = partial


        while head != None:
            insert(result, head.val)
            head = head.next

        result = result.next
        return result
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # traverse the list and look for nodes, where self.child is not None
        # keep the pointer to the previous node and to the original next node
        # merge a child list to the parent list - connect prev and next pointers
        # continue traversing until encountering another node where self.child is not None, 
        # or reaching the end of the main list
        
        current = head
        
        while current is not None:
            # check for child node
            if current.child is not None:
                # merge child list into the parent list
                self.merge(current)
                
            # move to the next node
            current = current.next
        
        return head
            
    
    def merge(self, current):
        child = current.child
        
        # traverse child list until we get the last node
        while child.next is not None:
            child = child.next
        
        # child is now pointing at the last node of the child list
        # we need to connect child.next to current.next, if there is any
        if current.next is not None:
            child.next = current.next
            current.next.prev = child
        
        # now, we have to connect current to the child list
        # child is currently pointing at the last node of the child list, 
        # so we need to use pointer (current.child) to get to the first node of the child list
        current.next = current.child
        current.child.prev = current
        
        # at the end remove self.child pointer
        current.child = None
        
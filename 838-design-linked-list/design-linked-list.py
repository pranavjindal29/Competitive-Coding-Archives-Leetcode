class Node:
    def __init__(self,val):
        self.val=val
        self.next=None


class MyLinkedList:

    def __init__(self):
        self.head=None
        self.length=0
        

    def get(self, index: int) -> int:
        if index>=self.length:
            return -1
        curr=self.head
        while index:
            curr=curr.next
            index-=1
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        newnode=Node(val)
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
        self.length+=1
        

    def addAtTail(self, val: int) -> None:
        newnode=Node(val)
        if self.head==None:
            self.head=newnode
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=newnode
        self.length+=1


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        elif index == 0:
           self.addAtHead(val)
        elif index == self.length:
           self.addAtTail(val)
        else:
            new_node = Node(val)
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node
            self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        elif index == 0:
           self.head = self.head.next
        elif index == self.length - 1:
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            curr.next = None
        else:
            curr = self.head
            i = index - 1
            while i:
                curr = curr.next
                i -= 1
            curr.next = curr.next.next
        self.length -= 1

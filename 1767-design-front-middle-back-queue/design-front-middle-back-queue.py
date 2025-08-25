class Node:
    def __init__(self, val = None):
        self.val = val
        self.prev = None
        self.next = None

class FrontMiddleBackQueue:

    def __init__(self):
        self.size = 0
        self.start = Node()
        self.end = Node()
        self.mid = self.start
        self.start.next = self.end
        self.end.prev = self.start
        self.posLeft, self.posRight, self.posMiddle = 'left', 'right', 'mid'

    def pushFront(self, val: int) -> None:
        node = Node(val)
        left, right = self.start, self.start.next
        node.prev, node.next = left, right
        left.next, right.prev = node, node
        self.__balanceMid(True, self.posLeft)

    def pushMiddle(self, val: int) -> None:
        node = Node(val)
        if self.size & 1: # 1 -> 3 -> 2 => add 4 bofore 3
            left, right = self.mid.prev, self.mid
        else: # 1 -> 2 => add 3 after 1
            left, right = self.mid, self.mid.next
        
        node.prev, node.next = left, right
        left.next, right.prev = node, node
        self.__balanceMid(True, self.posMiddle)

    def pushBack(self, val: int) -> None:
        node = Node(val)
        left, right = self.end.prev, self.end
        node.prev, node.next = left, right
        left.next, right.prev = node, node
        self.__balanceMid(True, self.posRight)

    def popFront(self) -> int:
        if self.isEmpty(): return -1
        node = self.start.next
        left, right = node.prev, node.next
        left.next, right.prev = right, left
        self.__balanceMid(False, self.posLeft)
        return node.val

    def popMiddle(self) -> int:
        if self.isEmpty(): return -1
        node = self.mid
        left, right = node.prev, node.next
        left.next, right.prev = right, left
        self.__balanceMid(False, self.posMiddle)
        return node.val
        
    def popBack(self) -> int:
        if self.isEmpty(): return -1
        node = self.end.prev
        left, right = node.prev, node.next
        left.next, right.prev = right, left
        self.__balanceMid(False, self.posRight)
        return node.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def __balanceMid(self, isAdd: bool, position: str):
        if isAdd:
            self.size += 1
            match position:
                case self.posMiddle:
                    if self.size & 1:
                        self.mid = self.mid.next
                    else:
                        self.mid = self.mid.prev
                case self.posLeft:
                    if self.size == 1:
                        self.mid = self.mid.next
                    elif self.size & 1 == 0:
                        self.mid = self.mid.prev 
                case self.posRight:
                    if self.size & 1:
                        self.mid = self.mid.next
        else:
            self.size -= 1
            if self.size == 0:
                self.mid = self.start
                return
            match position:
                case self.posMiddle:
                    if self.size & 1:
                        self.mid = self.mid.next
                    else:
                        self.mid = self.mid.prev
                case self.posLeft:
                    if self.size & 1:
                        self.mid = self.mid.next
                case self.posRight:
                    if self.size & 1 == 0:
                        self.mid = self.mid.prev

    def printNodes(self):
        cur = self.start
        values = []
        while cur:
            values.append(cur.val)
            cur = cur.next
        print(self.mid.val, [f'{v}' for v in values[1:-1]])
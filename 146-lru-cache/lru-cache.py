class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.size = capacity
        self.m = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def deleteNode(self, p):
        p.prev.next = p.next
        p.next.prev = p.prev

    def addNode(self, newnode):
        temp = self.head.next
        self.head.next = newnode
        newnode.prev = self.head
        newnode.next = temp
        temp.prev = newnode

    def get(self, key):
        if key not in self.m:
            return -1

        p = self.m[key]
        self.deleteNode(p)
        self.addNode(p)
        self.m[key] = self.head.next
        return self.head.next.val

    def put(self, key, value):
        if key in self.m:
            c = self.m[key]
            self.deleteNode(c)
            c.val = value
            self.addNode(c)
            self.m[key] = self.head.next
        else:
            if len(self.m) == self.size:
                prev = self.tail.prev
                self.deleteNode(prev)
                l = Node(key, value)
                self.addNode(l)
                del self.m[prev.key]
                self.m[key] = self.head.next
            else:
                l = Node(key, value)
                self.addNode(l)
                self.m[key] = self.head.next

# Example usage:
# cache = LRUCache(capacity)
# value = cache.get(key)
# cache.put(key, value)
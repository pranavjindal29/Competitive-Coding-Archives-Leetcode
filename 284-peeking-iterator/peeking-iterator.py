class PeekingIterator:
    def __init__(self, iterator):
        self.it = iterator
        self.pk = None

    def peek(self):
        if self.pk is None:
            self.pk = self.it.next()
        return self.pk

    def next(self):
        if self.pk is None:
            return self.it.next()
        ret = self.pk
        self.pk = None
        return ret

    def hasNext(self):
        return self.pk is not None or self.it.hasNext()
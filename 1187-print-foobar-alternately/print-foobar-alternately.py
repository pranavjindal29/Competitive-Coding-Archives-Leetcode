from threading import Event
class FooBar:
    def __init__(self, n):
        self.n = n
        self.e = Event()
        self.e1 = Event()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            printFoo()
            self.e.set() 
            self.e1.wait()
            self.e1.clear()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.e.wait()
            printBar()
            self.e1.set()
            self.e.clear() 
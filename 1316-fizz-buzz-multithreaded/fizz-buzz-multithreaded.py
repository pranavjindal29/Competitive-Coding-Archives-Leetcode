import threading as t

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.curr_num = 0
        self.update_fizbuzz_params()
        # Make Barrier responsible for incrementing the counter
        self.barrier = t.Barrier(4, action=self.update_fizbuzz_params)

    def update_fizbuzz_params(self):
        self.curr_num+=1
        self.is_fizz, self.is_buzz = self.curr_num % 3 == 0, self.curr_num % 5 == 0

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while self.curr_num <= self.n:
            if self.is_fizz and not self.is_buzz:
                printFizz()
            # wait for barier in the end so that the while loop condition 
            # is checked immediately after curr_num is incremented
            self.barrier.wait()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while self.curr_num <= self.n:
            if self.is_buzz and not self.is_fizz:
                printBuzz()
            self.barrier.wait()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while self.curr_num <= self.n:
            if self.is_fizz and self.is_buzz:
                printFizzBuzz()
            self.barrier.wait()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while self.curr_num <= self.n:
            if not self.is_fizz and not self.is_buzz:
                printNumber(self.curr_num)
            self.barrier.wait()
                
            
                
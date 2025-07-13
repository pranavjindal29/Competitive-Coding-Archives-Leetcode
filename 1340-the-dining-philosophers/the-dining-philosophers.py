from threading import Lock

class DiningPhilosophers:
    def __init__(self):
        self.forks = [Lock() for _ in range(5)]
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        
        left_fork, right_fork = self.forks[philosopher], self.forks[philosopher - 1]
        if philosopher%2: 
            first_fork, second_fork = right_fork, left_fork
        else:
            first_fork, second_fork = left_fork, right_fork

        with first_fork, second_fork:
            pickLeftFork()
            pickRightFork()
            eat()
            putRightFork()
            putLeftFork()
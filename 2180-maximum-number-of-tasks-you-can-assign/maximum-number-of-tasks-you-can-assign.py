class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], 
                      pills: int, strength: int) -> int:

        def cannot_complete(numTasks: int, p = pills)-> bool:
            cnt = 0 
            jobs = deque()
            
            for i in range(numTasks - 1, -1, -1): 
                while cnt < numTasks:
                    if tasks[cnt] > workers[i] + strength: break
                    jobs.append(tasks[cnt])
                    cnt += 1
                
                if not jobs:
                    return True
                
                if workers[i] >= jobs[0]:
                    jobs.popleft()
                elif p > 0:
                    jobs.pop()
                    p -= 1
                else:
                    return True

            return False


        tasks.sort()
        workers.sort(reverse = True)
        n = min(len(tasks), len(workers)) + 1

        return bisect_left(range(n), True, key = cannot_complete) - 1
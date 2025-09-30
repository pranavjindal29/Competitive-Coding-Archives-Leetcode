class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res = []
        avail = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(avail)
        unavail = []
        t = 0
        for i in range(len(tasks)):
            t = max(t, i)
            if len(avail) == 0:
                t = unavail[0][0]
            while unavail and t >= unavail[0][0]:
                time, weight, idx = heapq.heappop(unavail)
                heapq.heappush(avail, (weight, idx))
            weight, idx = heapq.heappop(avail)
            res.append(idx)
            heapq.heappush(unavail, (t + tasks[i], weight, idx))
        return res
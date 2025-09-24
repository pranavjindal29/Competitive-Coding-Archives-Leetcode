class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        et_heap = []
        for i, task in enumerate(tasks):
            heapq.heappush(et_heap, (task[0], task[1], i))

        order = []
        time = 0

        pt_heap = []
        while et_heap or pt_heap:
            while et_heap and et_heap[0][0] <= time:
                et, pt, i = heapq.heappop(et_heap)
                heapq.heappush(pt_heap, (pt, i))
            
            if pt_heap:
                pt, i = heapq.heappop(pt_heap)
                order.append(i)
                time += pt
            elif et_heap:
                time = et_heap[0][0]

        return order
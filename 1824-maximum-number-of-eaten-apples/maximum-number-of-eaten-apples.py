class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        heap : List[Tuple[int,int]] = []
        ans,day =0,0

        while day < n or heap:

            if day < n and apples[day] > 0:
                expire = days[day] + day - 1
                heapq.heappush(heap,(expire, apples[day]))

            while heap and heap[0][0] < day:
                heapq.heappop(heap)

            if heap:
                expire, cnt = heapq.heappop(heap)
                cnt -= 1
                ans += 1

                if cnt > 0 and expire > day:
                    heapq.heappush(heap,(expire,cnt))

            day += 1

        return ans
            
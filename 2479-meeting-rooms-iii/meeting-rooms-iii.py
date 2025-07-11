class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        avail, cnt, busy = list(range(n)), [0]*n, []
        for s, e in meetings:
            while busy and busy[0][0] <= s:
                _, r = heappop(busy)
                heappush(avail, r)
            duration = e - s
            if avail:
                r = heappop(avail)
                start = s
            else:
                end, r = heappop(busy)
                start = end
            heappush(busy, (start + duration, r))
            cnt[r] += 1
        return max(range(n), key=lambda x: cnt[x])
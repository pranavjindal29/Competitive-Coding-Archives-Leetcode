class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        from collections import defaultdict
        count = defaultdict(list)
        for n, t in zip(keyName, keyTime):
            t = float(t.replace(':', '.'))
            count[n].append(t)
        res = []
        # print(sorted(count['bb']))
        for n, times in count.items():
            times.sort()
            left, right = 0, 1
            leng = len(times)
            if leng <= 1:
                continue
            useage = 0
            while right < leng:
                t_left = times[left]
                t_right = times[right]
                while t_right - t_left > 1.001:
                    left += 1
                    usage = 0
                    t_left = times[left]
                
                usage = right - left + 1
                if usage >= 3:
                    res.append(n)
                    break
                right += 1
        return sorted(res)

        
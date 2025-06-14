class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        max_s = s
        for ch in s:
            if ch != '9':
                max_s = s.replace(ch, '9')
                break

        min_s = s
        for ch in s:
            if ch != '0':
                min_s = s.replace(ch, '0')
                break

        return int(max_s) - int(min_s)
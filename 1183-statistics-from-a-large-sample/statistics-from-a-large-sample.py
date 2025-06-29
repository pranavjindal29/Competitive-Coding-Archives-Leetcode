class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        def get_minimum():
            for i in range(len(count)):
                if count[i] > 0:
                    return i

        def get_maximum():
            for i in reversed(range(len(count))):
                if count[i] > 0:
                    return i
        
        def get_mean():
            return sum([e*i for i,e in enumerate(count)])/sum(count)
        
        def get_median():
            return (get_left_median(count) + get_right_median(count))/2
        
        def get_left_median(count):
            total = sum(count)
            cumulative = 0
            for i in range(len(count)):
                cumulative += count[i]
                if cumulative*2 == total:
                    return i + 0.5
                if cumulative*2 > total:
                    return i
        
        def get_right_median(count):
            return 255 - get_left_median(count[::-1])
        
        def get_mode():
            mode = 0
            for i in range(len(count)):
                if count[i] > count[mode]:
                    mode = i
            return mode

        return [get_minimum(), get_maximum(), get_mean(), get_median(), get_mode()]
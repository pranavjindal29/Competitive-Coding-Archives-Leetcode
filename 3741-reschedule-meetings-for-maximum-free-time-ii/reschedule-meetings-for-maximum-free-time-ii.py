class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        size = len(startTime)
        gapsArr,left = [],0
        for i in range(size):
            gap = startTime[i] - left
            gapsArr.append(gap)
            left = endTime[i]
        gapsArr.append(eventTime - endTime[-1])
        maxGapPrefix,maxGapSuffix = [0 for i in range(size)],[0 for i in range(size)]
        maxGapPrefix[0] = gapsArr[0]
        maxGapSuffix[size-1] = gapsArr[-1]

        # calculate left right max
        for i in range(1,size):
            maxGapPrefix[i]= max(maxGapPrefix[i-1],gapsArr[i])
        for i in range(size-1,0,-1):
            maxGapSuffix[i-1]= max(maxGapSuffix[i],gapsArr[i])
        
        ans = 0
        for i in range(size):
            curr = gapsArr[i]+gapsArr[i+1]
            barSize = endTime[i] - startTime[i]
            isValid = False
            if(i-1 >= 0):
                isValid = isValid or maxGapPrefix[i-1] >= barSize
            if(i+1 < size):
                isValid = isValid or maxGapSuffix[i+1] >= barSize
            if(isValid):
                curr += barSize
            ans = max(ans, curr)
        return ans
            
        
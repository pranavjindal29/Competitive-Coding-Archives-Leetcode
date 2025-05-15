class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n=len(groups)
        prev=groups[0]
        ans=[words[0]]
        i=1
        while i<n:
            while i<n and prev==groups[i]:
                i+=1
            if i<n:
                ans.append(words[i])
                prev=groups[i]
            i+=1
        return ans
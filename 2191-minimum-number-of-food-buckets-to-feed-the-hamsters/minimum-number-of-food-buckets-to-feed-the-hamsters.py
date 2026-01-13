class Solution:
    def minimumBuckets(self, street: str) -> int:
        street = list(street)
        ans = 0 
        for i, ch in enumerate(street): 
            if ch == 'H' and (i == 0 or street[i-1] != '#'): 
                if i+1 < len(street) and street[i+1] == '.': street[i+1] = '#'
                elif i and street[i-1] == '.': street[i-1] = '#'
                else: return -1
                ans=ans+1
        return ans
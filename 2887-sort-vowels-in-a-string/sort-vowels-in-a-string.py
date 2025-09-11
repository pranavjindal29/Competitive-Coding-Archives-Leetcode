class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        
        collected = [ch for ch in s if ch in vowels]
        
        collected.sort()
        
        result = []
        j = 0  
        for ch in s:
            if ch in vowels:
                result.append(collected[j])
                j += 1
            else:
                result.append(ch)
        
        return "".join(result)

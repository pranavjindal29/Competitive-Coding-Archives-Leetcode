class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        orig = set(wordlist) # original words O(1) lookup 
        case = {} # diff in case
        vowel = {} # diff in vowel
        
        for word in wordlist: 
            key = word.lower()
            case.setdefault(key, []).append(word)
            for c in "aeiou": key = key.replace(c, "*")
            vowel.setdefault(key, []).append(word)
        
        ans = []
        for word in queries: 
            if word in orig: ans.append(word)
            else: 
                key = word.lower()
                if key in case: ans.append(case[key][0])
                else: 
                    for c in "aeiou": key = key.replace(c, "*")
                    if key in vowel: ans.append(vowel[key][0])
                    else: ans.append("")
        return ans 
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word = [0]*len(words)
        targett = [len(word) for word in words]
        data = {}
        # val: char, key: corresponding index
        for i in range(len(words)):
            w = words[i][0]
            if w in data:
                data[w] += [i]
            else:
                data[w] = [i]
        
        for w in s:
            #print(data)
            if w in data:
                cv = data.pop(w)
                for index in cv:
                    word[index] += 1
                    target = word[index]
                    try:
                        new = words[index][target]
                        if new in data:
                            data[new] += [index]
                        else:
                            data[new] = [index]
                    except IndexError:
                        continue
        
        ans = 0
        for i in range(len(word)):
            ans += 1 if word[i] == targett[i] else 0
        
        return ans
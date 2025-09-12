class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge = {a:b for (a,b) in knowledge}
        words = [] 
        word = ''
        for c in s:
            if c == '(':
                words.append((word, 0))
                word = ''
            elif c == ')':
                words.append((word, 1))
                word = ''
            else:
                word += c
        words.append((word, 0))
        ret = ''
        for word, in_knowledge in words:
            if in_knowledge:
                ret += knowledge.get(word, '?')
            else:
                ret += word
        return ret



                
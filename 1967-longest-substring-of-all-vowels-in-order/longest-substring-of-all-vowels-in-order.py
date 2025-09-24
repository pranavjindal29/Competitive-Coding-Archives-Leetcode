class Solution:
    def get_bit(self, ch: str) -> int:
        match ch:
            case 'a': return 0
            case 'e': return 1
            case 'i': return 2
            case 'o': return 3
            case 'u': return 4
        return 0

    def longestBeautifulSubstring(self, word: str) -> int:
        output: int = 0
        left: int = 0
        cur_char: str = word[left]
        mask: int = 0
        for right in range(len(word)):
            if (cur_char != word[right]) and (
                (cur_char == 'a' and word[right] != 'e')
                or (cur_char == 'e' and word[right] != 'i')
                or (cur_char == 'i' and word[right] != 'o')
                or (cur_char == 'o' and word[right] != 'u')
                or (cur_char == 'u')
            ):
                left = right
                mask = 0
            cur_char = word[right]
            mask |= (1 << self.get_bit(cur_char))
            if mask == 31: output = max(output, right - left + 1)
        return output
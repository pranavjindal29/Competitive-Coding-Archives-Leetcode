class Solution:
    def maxRepOpt1(self, text: str) -> int:
        m = defaultdict(int)
        available_chars = Counter(text)
        left = ans = swapped = 0

        def possible_to_swap_2(m, available_chars):
            if len(m) > 2:
                return False

            keys = list(m.keys())
            for key in keys:
                other_key = keys[1] if key == keys[0] else keys[0]
                if m[key] <= 1 and available_chars.get(other_key, 0) > 0:
                    return True

            return False

        for right in range(len(text)):
            available_chars[text[right]] -= 1
            if available_chars[text[right]] <= 0:
                del available_chars[text[right]]

            m[text[right]] += 1
            if len(m.keys()) == 1 or possible_to_swap_2(m, available_chars):
                ans = max(ans, right - left + 1)
            else:
                m[text[left]] -= 1
                if m[text[left]] <= 0:
                    del m[text[left]]

                available_chars[text[left]] += 1
                left += 1
        
        return ans
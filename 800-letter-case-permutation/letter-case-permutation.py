class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        self.backtrack("", s, result)
        return result

    def backtrack(self, output: str, input_str: str, result: List[str]) -> None:
        if not input_str:
            result.append(output)
            return
        c = input_str[0]
        remaining = input_str[1:]
        if c.isdigit():
            self.backtrack(output + c, remaining, result)
        else:
            self.backtrack(output + c.lower(), remaining, result)
            self.backtrack(output + c.upper(), remaining, result)
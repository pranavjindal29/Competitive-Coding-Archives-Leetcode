class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        def get_cur_sum(num: int) -> int:
            i, cur_sum = 1, 0
            while i <= 20 and num:
                if num & 1: cur_sum += i
                i += 1
                num >>= 1
            return cur_sum
        
        max_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if max_sum < desiredTotal: return False

        @cache
        def dp(choosen_int: int, player: int) -> bool:
            cur_sum = get_cur_sum(choosen_int)
            for i in range(maxChoosableInteger):
                if choosen_int & (1 << i): continue
                if cur_sum + i + 1 >= desiredTotal or \
                   not dp(choosen_int | (1 << i), player ^ 1):
                   return True
            return False
        
        return dp(0, 0)
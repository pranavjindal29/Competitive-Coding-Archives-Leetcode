class Solution:
    def rotatedDigits(self, n: int) -> int:
        ROTATED = {
            0: '0',
            1: '1',
            2: '5',
            3: None,
            4: None,
            5: '2',
            6: '9',
            7: None,
            8: '8',
            9: '6'
        }

        res = 0
        for i in range(1, n + 1):
            original_num = i
            rotated_num = ''
            while i > 0:
                digit = i % 10
                rotated_digit = ROTATED[digit]

                if not rotated_digit:
                    rotated_num = original_num
                    break
                
                rotated_num = rotated_digit + rotated_num

                i //= 10
            
            i = original_num

            if int(rotated_num) != i: res += 1
        
        return res
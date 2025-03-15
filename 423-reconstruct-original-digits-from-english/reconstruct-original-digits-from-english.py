
class Solution:
    def originalDigits(self, s: str) -> str:
        # Count occurrences of each letter in the string
        char_count = Counter(s)
        
        # Initialize a list to store counts of each digit
        count = [0] * 10
        
        # Unique letters for each digit
        count[0] = char_count['z']  # 'z' is unique to "zero"
        count[2] = char_count['w']  # 'w' is unique to "two"
        count[4] = char_count['u']  # 'u' is unique to "four"
        count[6] = char_count['x']  # 'x' is unique to "six"
        count[8] = char_count['g']  # 'g' is unique to "eight"
        
        # Letters that appear in multiple digits
        count[3] = char_count['h'] - count[8]  # 'h' is in "three" and "eight"
        count[5] = char_count['f'] - count[4]  # 'f' is in "five" and "four"
        count[7] = char_count['s'] - count[6]  # 's' is in "seven" and "six"
        count[1] = char_count['o'] - count[0] - count[2] - count[4]  # 'o' is in "one", "zero", "two", "four"
        count[9] = char_count['i'] - count[5] - count[6] - count[8]  # 'i' is in "nine", "five", "six", "eight"
        
        # Reconstruct the digits
        result = ''.join(str(i) * count[i] for i in range(10))
        
        return result
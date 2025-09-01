class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        zero = binary.count('0')                         
        zero_idx = binary.index('0') if zero > 0 else 0  
        one = len(binary) - zero_idx - zero
        return f"{binary[:zero_idx]}{'1'*(zero-1)}{'0'*min(zero, 1)}{'1'*one}"
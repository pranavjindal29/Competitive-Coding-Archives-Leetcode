class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        balance = 1
        for node in preorder.split(','):
            if balance <= 0:
                return False
            if node == '#':
                balance -= 1
            else:
                balance += 1
        return balance == 0
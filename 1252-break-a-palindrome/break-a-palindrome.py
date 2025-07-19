class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1:
            return ""
        else:
            for x in range(len(palindrome)):
                s = ""
                if palindrome[x]!="a":
                    s+=palindrome[:x]+'a'+palindrome[x+1:]
                    if s!=s[::-1]:
                        return s
            s = palindrome[:len(palindrome)-1]+"b"
            return s
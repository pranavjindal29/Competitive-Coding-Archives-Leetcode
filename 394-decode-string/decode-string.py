class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        i = len(s)-1
        while(i>=0):
            if s[i]=="]" or s[i].isalpha():
                st.append(s[i])
            elif s[i]=="[":
                sub = ""
                while(st[-1]!="]"):
                    sub+=st.pop()
                st.pop()
                st.append(sub)
            elif 48<=ord(s[i])<=57:
                n = s[i]
                while(i>0 and 48<=ord(s[i-1])<=57):
                    n += s[i-1]
                    i-=1
                subst2 = st.pop()
                st.append(int(n[::-1]) * subst2)
            i-=1
        ans = ""
        st.reverse()
        for i in st:
            ans+=i
        return ans
        
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:      
        m = {}

        for i in range(len(s)):
            m[s[i]] = t[i]

        st = ""
        for i in range(len(s)):
            st = st + m[s[i]]

        n = {}

        for i in range(len(t)):
            n[t[i]] = s[i]

        st1 = ""
        for i in range(len(t)):
            st1 = st1 + n[t[i]]
        
        if st == t and st1 == s:
            return True
        
        return False
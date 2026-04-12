class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char = {}
        t_char = {}
        if len(s) != len(t):
            return False
        s = s.lower()
        t = t.lower()
        for i in range(len(s)):
            s_char[s[i]] = 1 + s_char.get(s[i], 0)
            t_char[t[i]] = 1 + t_char.get(t[i], 0)
        
        return s_char == t_char
        

        

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        
        if len(s) != len(t):
            return False
        else:
            s = s.lower()
            t = t.lower()
            for i in range(len(s)):
                s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
                t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
        
        if s_dict == t_dict:
            return True
        else:
            return False
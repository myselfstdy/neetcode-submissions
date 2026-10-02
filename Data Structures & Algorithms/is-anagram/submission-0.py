class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        fre = {}
        for ch in s:
            fre[ch] = fre.get(ch,0)+1
        for ch in t:
            if ch not in fre:
                return False
            fre[ch] -=1
            if fre[ch] <0:
                return False
        return True
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ''' maxi =0
        for i in range(len(s)):
            se = set()
            for j in range(i,len(s)):
                if s[j] in se:
                    break
                se.add(s[j])
                maxi = max(maxi,j-i+1)
        return maxi '''

        fre  = {}
        left = 0
        maxi = 0
        for r in range(len(s)):
            ch = s[r]
            fre[ch] = fre.get(ch,0)+1
            while fre[s[r]] >1 :
                fre[s[left]] -=1
                left+=1
            maxi = max(maxi,r-left+1)
        return maxi
        